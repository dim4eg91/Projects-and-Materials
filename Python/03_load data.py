import psycopg2
import mail_config

greenplum = psycopg2.connect(
    database=mail_config.db_name,
    user=mail_config.user,
    password=mail_config.password,
    host=mail_config.host,
    port=mail_config.port
)

gp_cursor = greenplum.cursor()
file = open('D:/Mail_read_files/email_body.csv', 'r', encoding='utf-8')


def load_data_to_temp_table():
    answer = input('Точно загрузить новую пачку данных?\nНапишите "да" или "нет"\n\nОтвет: ')
    if answer == 'да':
        gp_cursor.copy_from(file, 'email_body_temp', sep=';')
        greenplum.commit()
    else:
        return None


load_data_to_temp_table()
file.close()
gp_cursor.close()
greenplum.close()
