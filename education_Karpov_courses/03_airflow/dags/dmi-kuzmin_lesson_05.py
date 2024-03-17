"""
Lesson 5

Создайте в GreenPlum'е таблицу с названием "<ваш_логин>_ram_location" с полями id, name, type, dimension, resident_cnt.

С помощью API (https://rickandmortyapi.com/documentation/#location) найдите три локации сериала "Рик и Морти" с наибольшим количеством резидентов.
Запишите значения соответствующих полей этих трёх локаций в таблицу. resident_cnt — длина списка в поле residents.
"""

from airflow import DAG
from airflow.utils.dates import days_ago

from dmi_kuzmin_plugins.dmi_kuzmin_ram_locations_operator import DmikuzminRamLocationsOperator

DEFAULT_ARGS = {
    'start_date': days_ago(2),
    'owner': 'dmi-kuzmin',
    'poke_interval': 600
}

with DAG("dmi-kuzmin_lesson_05",
         schedule_interval='@daily',
         default_args=DEFAULT_ARGS,
         max_active_runs=1,
         tags=['dmi-kuzmin']
         ) as dag:
    location = DmikuzminRamLocationsOperator(task_id='API_DB',
                                              api_url='https://rickandmortyapi.com/api/location/',
                                              table_name='dmi_kuzmin_ram_location'
                                              )

    location
