"""
DAG для задания 4 урока ETL.

Работать с понедельника по субботу, но не по воскресеньям (можно реализовать с помощью расписания или операторов ветвления)

Используйте соединение 'conn_greenplum'

Забирать из таблицы articles значение поля heading из строки с id, равным дню недели ds (понедельник=1, вторник=2, ...)
Выводить результат работы в любом виде: в логах либо в XCom'е
Даты работы дага: с 1 марта 2022 года по 14 марта 2022 года
"""

from airflow import DAG
import logging
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import pendulum

default_args = {
    'owner': 'dmi-kuzmin',
    'poke_interval': 60
}

with DAG('dmi-kuzmin_lesson_04',
         start_date=datetime(2022, 3, 1),
         end_date=datetime(2022, 3, 14),
         schedule_interval='0 12 * * 1-6',
         default_args=default_args,
         max_active_runs=1,
         tags=['dmi-kuzmin']
         ) as dag:
    start = DummyOperator(task_id='start', dag=dag)
    end = DummyOperator(task_id='end', dag=dag)


    def get_data_from_bd_func():
        dw = datetime.now().isoweekday()
        logging.info(f'Current weekday: {dw}')
        pg_hook = PostgresHook(postgres_conn_id='conn_greenplum')
        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        cursor.execute(f'SELECT heading FROM articles WHERE id = {dw}')
        query_res = cursor.fetchall()  # полный результат
        for r in query_res:
            logging.info(r)
            print(r)


    # one_string = cursor.fetchone()[0]  # если вернулось единственное значение

    get_data_from_bd = PythonOperator(
        task_id='get_data_from_bd',
        python_callable=get_data_from_bd_func,
        dag=dag

    )

    start >> get_data_from_bd >> end
