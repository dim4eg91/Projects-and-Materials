import imaplib
import email
from email.header import decode_header
import base64
import psycopg2
import re
from sqlalchemy import create_engine

import pandas as pd

import config
import mail_read_functions as func
from config import *

from bs4 import BeautifulSoup
import re

# -----------------------------------------------------------------
# Conn для БД
#
connection = psycopg2.connect(
    database=db_name,
    user=user,
    password=password,
    host=host,
    port=port
)

# Подключение к почте

mail_pass = config.mail_pass
username = config.username
imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)
imap.select("INBOX")  # выбор папки Входящие в почте
unseen_mails = imap.search(None, 'UNSEEN')  # поиск непрочитанных писем
unseen_mails_str = str(unseen_mails[1])

# print('Непрочитанные письма: ', unseen_mails_str, '\n')  # показ непрочитанных писем

print('Непрочитанные письма: ',
      func.parsing_list_unseen_email(unseen_mails_str))  # формирование списка непрочитанных писем

# присвоение определенного номера письма переменной

res, msg = imap.fetch(b'2552', '(RFC822)')  # Для метода search по порядковому номеру письма
msg = email.message_from_bytes(msg[0][1])

print('Заголовок письма:\n', decode_header(msg["Subject"])[0][0].decode(), '\n')  # чтение заголовка письма

# print(msg.get_payload())
# print(msg.is_multipart())  # проверка тела письма, является ли оно сложным (метод is_multipart())


# for part in msg.walk():
#     if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'html':
#         print(base64.b64decode(part.get_payload()).decode())


body = base64.b64decode(msg.get_payload()).decode('utf-8')  # тело (содержимое) письма

st = {}
product_name = []
count_and_price = []
count = []
price = []
total_price = []
order_date = ''

# пишу в файл тело письма, чтобы далее его распарсить и сделать DataFrame
with open('D:/pythonProject/simple.txt', 'w', encoding='utf-8') as f:
    f.write(body)

with open('D:/pythonProject/simple.txt', 'r', encoding='utf-8') as f:
    line = f.readline()  # считываем первую строку
    while line != '':  # пока не конец файла
        if 'Приход' in line:
            for i in range(3):
                line = f.readline()
            order_date = line.strip()
        if 'product-name' in line:
            line = f.readline()
            product_name.append(line.strip())
            for i in range(5):
                line = f.readline()
            count.append(func.parsing_quantity_and_price_per_one(line.strip())[0])
            price.append(round(func.parsing_quantity_and_price_per_one(line.strip())[1], 2))
            count_and_price.append(line.strip())
            for i in range(8):
                line = f.readline()
            total_price.append(line.strip())
        line = f.readline()  # читаем новую строку

st.setdefault('product_name', product_name)
st.setdefault('count', count)
st.setdefault('price', price)
st.setdefault('total_price', total_price)

df = pd.DataFrame(st)

# Трансформация - необходимо распарсить поле count_and_price. поле total_price сделать int

df['total_price'] = df['total_price'].astype(float)

print(df['total_price'].dtype)


# настройки подключения БД
# engine = create_engine('postgresql://postgres:fhixvlh1@localhost:5432/postgres')
# df.to_sql('email_body', engine)


def join_data_from_sprv():
    "Функция для каждого значения DF заполняет его последнюю колонку значениями из справочника sprv"

    def find_key_by_value(spravochnic, value: str):
        """
        Функция ищет ключ в словаре по заданному переданному значению.
        :param spravochnic: Словарь, по которому идет поиск
        :param value: Значение, для которого нужно вернуть ключ
        :return: Ключ для переданного значения
        """
        for key, val_list in spravochnic.items():
            if value in val_list:
                return key
        return None

    df['product_category'] = df['product_name'].apply(lambda x: find_key_by_value(func.product_category_table, x))


join_data_from_sprv()
df['order_date'] = order_date
print(df)


def get_product_categories_table():
    """
    Функция подключается к БД и сохраняет в DF таблицу категорий продуктов, просит заполнить ее по новому
    списку продуктов и заливает в БД.
    :return: None
    """
    engine = create_engine('postgresql://postgres:fhixvlh1@localhost:5432/postgres')
    # pct = df.to_sql('product_categories_table', engine)
    pct_df = pd.read_sql_query('select * from product_categories_table', connection)
    connection.close()
    return pct_df


prc_temp = get_product_categories_table()
print(prc_temp)


def fill_product_categories_table(prc_temp, df):
    product_category_dict = {
        '1': "Молочка",
        '2': "Мясо и птица",
        '3': "Рыба и морепродукты",
        '4': "Овощи",
        '5': "Хлеб",
        '6': "Соусы и приправы",
        '7': "Непрод",
        '8': "Алкоголь"
    }
    temp = {}
    product_name_temp = []
    product_category_temp = []
    for i in df['product_name']:
        if i not in prc_temp:
            a = input(f"Какая категория продука - {i} - ")
            product_name_temp.append(i)
            product_category_temp.append(product_category_dict[a])
    temp.setdefault('product_name', product_name_temp)
    temp.setdefault('product_category', product_category_temp)
    temp_df = pd.DataFrame(temp)
    # new_prod_cat_table = prc_temp + temp_df
    return temp_df


b = fill_product_categories_table(prc_temp, df)

print(b)
