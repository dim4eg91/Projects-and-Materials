import pandas as pd
from sqlalchemy import create_engine
import mail_config
import psycopg2
from datetime import datetime


# настройки подключения БД


def write_df_to_postgres_table():
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="fhixvlh1",
        host="127.0.0.1",
        port=5432
    )
    cur = connection.cursor()
    f = open('D:/Mail_read_files/email_body.csv', 'r', encoding='utf-8')
    if cur.copy_from(f, 'public.email_body_temp', sep=';') is True:
        print('[INFO] Successful write DataFrame to Postgres table')
    else:
        print('[INFO] Error write DataFrame to Postgres table')
    f.close()
    connection.close()


# write_df_to_postgres_table()


# cur.copy_from(f, 'email_body_temp', sep=';')
# f.close()
# connection.close()

connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="fhixvlh1",
    host="127.0.0.1",
    port=5432
)
cur = connection.cursor()
f = open('D:/Mail_read_files/email_body.csv', 'r', encoding='utf-8')
cur.copy_from(f, 'email_body_temp', sep=';')
f.close()
connection.close()
