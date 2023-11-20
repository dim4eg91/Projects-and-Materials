import psycopg2

greenplum = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="fhixvlh1",
    host="localhost",
    port=5432
)

gp_cursor = greenplum.cursor()
f = open('D:/Mail_read_files/email_body.csv', 'r', encoding='utf-8')
gp_cursor.copy_from(f, 'email_body', sep=';')
greenplum.commit()
f.close()
gp_cursor.close()
greenplum.close()
