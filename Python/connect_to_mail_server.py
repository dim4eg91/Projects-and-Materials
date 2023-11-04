# скрипт подключения к почтовому серверу mail.ru
#
#
#
#
#


import config
import imaplib
import email
from email.header import decode_header
import base64
import mail_read_functions as func



mail_pass = config.mail_pass
username = config.username

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


imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)
imap.select("INBOX")  # выбор папки Входящие в почте
unseen_mails = imap.search(None, 'UNSEEN')  # поиск непрочитанных писем
unseen_mails_str = str(unseen_mails[1])

# print('Непрочитанные письма: ', unseen_mails_str, '\n')  # показ непрочитанных писем

# print('Непрочитанные письма: ',
#       func.parsing_list_unseen_email(unseen_mails_str))  # формирование списка непрочитанных писем

print('Непрочитанные письма: ',
      parsing_list_unseen_email(unseen_mails_str))  # формирование списка непрочитанных писем

res, msg = imap.fetch(b'3061', '(RFC822)')  # Для метода search по порядковому номеру письма
msg = email.message_from_bytes(msg[0][1])
print('Заголовок письма:\n', decode_header(msg["Subject"])[0][0].decode(), '\n')  # чтение заголовка письма
# print(type(decode_header(msg["Subject"])[0][0].decode()))
# s = ''.join(str(x) for x in body)
# body = base64.b64decode(msg.get_payload()).decode('utf-8')  # тело (содержимое) письма
print(msg.is_multipart())


for part in msg.walk():
    print(part.get_content_type())

for part in msg.walk():
    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'html':
        print(base64.b64decode(part.get_payload()).decode())

