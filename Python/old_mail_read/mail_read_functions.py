import imaplib
import email


def parsing_list_unseen_email(unseen_emails: str):
    """
    Функция принимает на вход строку непрочитанных писем и возвращает список ID таких писем
    :param unseen_emails: объект, который содержит непрочитанные письма
    :return: список ID непрочитанных писем
    """
    # Для отладки функции
    # s = "b'234 235 236"
    lst_id_unseen_emails = []
    simple_emails = []  # простые письма, которые можно обработать
    digit_char = ''
    for i in range(len(unseen_emails)):
        if unseen_emails[i].isdigit():
            digit_char += unseen_emails[i]
        else:
            if digit_char != '':
                lst_id_unseen_emails.append(digit_char)
                digit_char = ''
    lst_id_unseen_emails.append(digit_char)

    for i in range(len(lst_id_unseen_emails)):
        res, msg = imap.fetch(f"b'{i}', '(RFC822)'")  # Для метода search по порядковому номеру письма
        msg = email.message_from_bytes(msg[0][1])
        if not msg.is_multipart():
            simple_emails.append(lst_id_unseen_emails[i])



    print('Заголовок письма:\n', decode_header(msg["Subject"])[0][0].decode(), '\n')  # чтение заголовка письма

    return lst_id_unseen_emails





def globus_email(lst_id_unseen_emails: list):
    # возможно нужно будет передавать + 1 переменную (ID)
    """
    Функция обработки письма от Globus.
    Подобное письмо имеет свою уникальную структуру html - важно для парсера!
    :param lst_id_unseen_emails: список ID непрочитанных писем
    :return:
    """
    pass


def vkusvill_email(lst_id_unseen_emails: list):
    # возможно нужно будет передавать + 1 переменную (ID)
    """
    Функция обработки письма от Vkusvill.
    Подобное письмо имеет свою уникальную структуру html - важно для парсера!
    :param lst_id_unseen_emails: список ID непрочитанных писем
    :return:
    """
    pass


def parsing_quantity_and_price_per_one(s: str):
    """
    Функция парсит входную строку и возвращает переменную 1 - количество единиц товара и переменную 2 - цену за единицу товара
    :param s: Входная строка после первоначального парсинга
    :return:
    """
    quantity = 0
    a = s[s.find('х') + 2:]
    price_per_one = float(a)
    dig = ''
    for i in s:
        if i.isdigit():
            dig += i
        else:
            quantity = int(dig)
            return quantity, price_per_one
    return quantity, price_per_one


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

    # df['Task_type'] = df['CR_body'].apply(lambda x: find_key_by_value(product_category_table, x))


import pandas as pd

# data = {'CR_name': ['DEA-498', 'DEA-503', 'DEA-519'], 'CR_body': ['Релиз', 'Вывод', 'Обновление'], 'Task_type': ''}
# df = pd.DataFrame(data)
# print(df)
# print()
# sprv = {'Баг': ['Релиз', 'Обновление'], 'Стори': ['Вывод']}
#
#
# join_data_from_sprv()
# print(df)


#  Словарь - справочник
product_category_table = {
    'Овощи': ['МОРКОВЬ ПО-КОР.150ГР'],
    'Молочка': ['НАП NEMOLOKO ГРЕЧ 1Л', 'НАП РИСОВ КЛАСС 1Л', 'НАП ОВС КЛАСС 3,2%', 'НАП ОВС ШОКОЛ 1Л'],
    'Мясо и птица': ''
}
