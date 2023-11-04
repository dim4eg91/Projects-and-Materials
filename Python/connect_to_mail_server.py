# EXTRACT
# скрипт подключения к почтовому серверу mail.ru

# Импорт библиотек и файлов

import imaplib
import email
from email.header import decode_header
import base64
import mail_config

# Параметры для подключения к почтовому серверу

mail_pass = mail_config.mail_pass
username = mail_config.username


# Блок 0 - функции

def parsing_list_unseen_email(unseen_emails: str):
    """
    Функция принимает на вход строку непрочитанных писем и возвращает список ID таких писем
    :param unseen_emails: объект, который содержит непрочитанные письма
    :return: список ID непрочитанных писем
    """

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
    lst_id_unseen_emails.pop()

    # for i in range(len(lst_id_unseen_emails)):
    #     res, msg = imap.fetch(f"b'{i}', '(RFC822)'")  # Для метода search по порядковому номеру письма
    #     msg = email.message_from_bytes(msg[0][1])
    #     if not msg.is_multipart():
    #         simple_emails.append(lst_id_unseen_emails[i])
    #
    #
    #
    # print('Заголовок письма:\n', decode_header(msg["Subject"])[0][0].decode(), '\n')  # чтение заголовка письма

    return lst_id_unseen_emails


def parsing_list_unseen_email_to_bytes(unseen_emails: str):
    """
    Функция принимает на вход строку непрочитанных писем и возвращает список ID таких писем
    :param unseen_emails: объект, который содержит непрочитанные письма
    :return: список ID непрочитанных писем
    """

    lst_id_unseen_emails = []
    digit_char = ''
    for i in range(len(unseen_emails)):
        if unseen_emails[i].isdigit():
            digit_char += f"b'{unseen_emails[i]}"
        else:
            if digit_char != '':
                lst_id_unseen_emails.append(digit_char)
                digit_char = ''
    lst_id_unseen_emails.append(digit_char)
    lst_id_unseen_emails.pop()
    return lst_id_unseen_emails


# Блок 1 - подключение к почтовому серверу и получение списка непрочитанных писем

imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)
imap.select("INBOX")  # выбор папки Входящие в почте
unseen_mails = imap.search(None, 'UNSEEN')  # поиск непрочитанных писем
unseen_mails_str = str(unseen_mails[1])

print('Непрочитанные письма: ',
      parsing_list_unseen_email(unseen_mails_str))  # формирование списка непрочитанных писем

#
# print('Непрочитанные письма: ',
#       parsing_list_unseen_email(unseen_mails_str))  # формирование списка непрочитанных писем

# find_first_actual_unseen_email(parsing_list_unseen_email(unseen_mails_str))

res, msg = imap.fetch(b'3063', '(RFC822)')  # Для метода search по порядковому номеру письма
# print(type(b'3061'))
msg = email.message_from_bytes(msg[0][1])
print('Заголовок письма:\n', decode_header(msg["Subject"])[0][0].decode(), '\n')  # чтение заголовка письма

# print(type(decode_header(msg["Subject"])[0][0].decode()))

# body = base64.b64decode(msg.get_payload()).decode('utf-8')  # тело (содержимое) письма
# s = ''.join(str(x) for x in body)


print(msg.is_multipart())  # проверка письма на вложенность
#
# for part in msg.walk():
#     print(part.get_content_type())
#
for part in msg.walk():
    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'html':
        print(base64.b64decode(part.get_payload()).decode())

# определяем, от какого магазина чек - нужно для имени temp файла


# with open('D:/pythonProject/simple.txt', 'r', encoding='utf-8') as f:
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

# пишу в файл тело письма, чтобы далее его распарсить и сделать DataFrame
with open('D:/Mail_read_files/simple.txt', 'w', encoding='utf-8') as f:
    for part in msg.walk():
        if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'html':
            f.write(base64.b64decode(part.get_payload()).decode())
