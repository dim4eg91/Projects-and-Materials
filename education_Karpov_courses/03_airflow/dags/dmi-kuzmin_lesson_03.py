"""
DAG для задания 3 урока ETL.

Внутри создать даг из нескольких тасков:
— DummyOperator
— BashOperator с выводом даты
— PythonOperator с выводом даты
"""

from airflow import DAG
from airflow.utils.dates import days_ago
import logging
import datetime

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'start_date': days_ago(2),
    'owner': 'dmi-kuzmin',
    'poke_interval': 600
}

with DAG('dmi-kuzmin_lesson_03',
         schedule_interval='@daily',
         default_args=default_args,
         max_active_runs=1,
         tags=['dmi-kuzmin']
         ) as dag:
    dummy = DummyOperator(task_id='dummy_start')

    bash_date = BashOperator(
        task_id='bash_print_date',
        bash_command='echo {{ ds }}',
        dag=dag
    )

    def print_current_date_func():
        print(f'The current date is {datetime.date.today()}')

    python_date = PythonOperator(
        task_id='python_print_date',
        python_callable=print_current_date_func,
        dag=dag

    )

    dummy >> bash_date >> python_date



dag.doc_md = __doc__

dummy.doc_md = """Просто dummy оператор"""
bash_date.doc_md = """Выводит в лог execution_date"""
python_date.doc_md = """Выводит в лог execution_date"""
