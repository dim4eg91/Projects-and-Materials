"""
Тестовый даг -3
"""

from airflow import DAG
from airflow.utils.dates import days_ago
import logging


from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'start_date': days_ago(2),
    'owner': 'dmi-kuzmin',
    'poke_interval': 600
}

with DAG('dmi-kuzmin_test',
         schedule_interval='@daily',
         default_args=default_args,
         max_active_runs=1,
         tags=['dmi-kuzmin']
         ) as dag:
    dummy = DummyOperator(task_id='dummy')

    echo = BashOperator(
        task_id='echo',
        bash_command='echo {{ ds }}',
        dag=dag
    )


    def hello_world_func():
        logging.info('Hello man!')


    hello_world = PythonOperator(
        task_id='hello_world',
        python_callable=hello_world_func,
        dag=dag
    )

    dummy >> [echo, hello_world]

