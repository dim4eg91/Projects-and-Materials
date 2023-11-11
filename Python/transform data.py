import pandas as pd
from sqlalchemy import create_engine
import mail_config
import psycopg2

st = {}
product_name = []
count_and_price = []
count = []
price = []
total_price = []
od = []
shop = []


def transform_data_vkusvill():
    """
    Функция обработки письма от Vkusvill.
    Подобное письмо имеет свою уникальную структуру html - важно для парсера!
    :return:
    """
    with open(r'D:/Mail_read_files/email_body.txt', 'r', encoding='utf-8') as f:
        line = f.readline()  # считываем первую строку
        while line != '':  # пока не конец файла
            if 'АО "Вкусвилл"<br />' in line:
                shop_name = 'АО "Вкусвилл"'
                for i in range(14):
                    line = f.readline()
                order_date = line[:line.find('<')].strip()
            if 'width="40%"' in line:
                od.append(order_date)
                shop.append(shop_name)
                for i in range(2):
                    line = f.readline()
                    if ',кг' in line:
                        product = line[:line.find(',кг')].strip('[M] ')
                        product_name.append(product)
                    elif ',шт' in line:
                        product = line[:line.find(',шт')].strip('[M] ')
                        product_name.append(product)
                for i in range(2):
                    line = f.readline().replace(',', '.')
                price.append(float(line.strip()))
                for i in range(2):
                    line = f.readline().replace(',', '.')
                count.append(float(line.strip()))
                line = f.readline()
                a = line[line.find('top') + 5:line.find('colspan')]
                total_price.append(float((a[:a.find('<')]).replace(',', '.')))
            line = f.readline()


transform_data_vkusvill()

# with open('D:/Mail_read_files/email_body.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()  # считываем первую строку
#     while line != '':  # пока не конец файла
#         if 'Приход' in line:
#             for i in range(3):
#                 line = f.readline()
#             order_date = line.strip()
#         if 'product-name' in line:
#             line = f.readline()
#             product_name.append(line.strip())
#             for i in range(5):
#                 line = f.readline()
#             count.append(func.parsing_quantity_and_price_per_one(line.strip())[0])
#             price.append(round(func.parsing_quantity_and_price_per_one(line.strip())[1], 2))
#             count_and_price.append(line.strip())
#             for i in range(8):
#                 line = f.readline()
#             total_price.append(line.strip())
#         line = f.readline()  # читаем новую строку


st.setdefault('product_name', product_name)
st.setdefault('count', count)
st.setdefault('price', price)
st.setdefault('total_price', total_price)
st.setdefault('order_date', od)
st.setdefault('shop_name', shop)

df = pd.DataFrame(st)
print(df)
df.to_csv('D:/Mail_read_files/email_body.csv', sep=',', encoding='utf-8')

# настройки подключения БД
connection = psycopg2.connect(
    database=mail_config.db_name,
    user=mail_config.user,
    password=mail_config.password,
    host=mail_config.host,
    port=mail_config.port
)


def write_df_to_postgres_table():
    engine = create_engine('postgresql://postgres:fhixvlh1@localhost:5432/postgres')
    if df.to_sql('public.email_body_temp', engine) is True:
        print('[INFO] Successful write DataFrame to Postgres table')
    else:
        print('[INFO] Error write DataFrame to Postgres table')


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

    # df['product_category'] = df['product_name'].apply(lambda x: find_key_by_value(func.product_category_table, x))

# join_data_from_sprv()
# print(df)
