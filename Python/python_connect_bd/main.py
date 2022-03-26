import psycopg2
from config import host, user, password, db_name, port

try:
    #  connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )

    connection.autocommit = True

    # the cursor from performing database operation
    #  cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        print(f'Server version: {cursor.fetchone()}')

    # create new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         first_name varchar(50) NOT NULL,
    #         nick_name varchar(50) NOT NULL);"""
    #     )
    #     #connection.commit()
    #     print("[INFO] Table created successfully")

    # insert data to a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT into users(first_name, nick_name) VALUES
    #         ('Олег', 'Ba');"""
    #     )
    #     #connection.commit()
    #     print("[INFO] Data was successfully inserted")

    # print data
    with connection.cursor() as cursor:
        cursor.execute(
            """select * from dwh.geography_dim;"""
        )

        print("[INFO] Data ready")
        result = cursor.fetchall()

    # delete table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    #     #connection.commit()
    #     print("[INFO] Table deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

# Write into file as csv

with open('D:\python_connect_bd\geography_dim.csv', 'w') as f:
    for row in result:
        for i in row:
            f.write(str(i) + ';')
        f.write('\n')