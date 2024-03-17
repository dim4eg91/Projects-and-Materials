import requests
import logging

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.hooks.http_hook import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook


class DmikuzminRickMortyHook(HttpHook):
    """
    Класс для работы с БД
    """

    def __init__(self, result: list, table_name: str, **kwargs) -> None:
        """
        Функция инициализации
        :param result: результат
        :param table_name: таблица в БД
        :param kwargs: прочие параметры
        """
        super().__init__(**kwargs)
        self.result = result
        self.table_name = table_name

    def insert_gp(self):
        """
        Функция работы с Greenplum

        На каждом шаге происходит логирование действий:
        - инициализация pg_hook
        - создание таблицы, если таблица не существует
        - очистка таблицы, если таблица существует
        - запись данных
        :return: None
        """
        pg_hook = PostgresHook(postgres_conn_id='conn_greenplum_write')
        logging.warning('Initialise pg_hook')

        pg_hook.run(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id TEXT,
                name TEXT,
                type TEXT,
                dimension TEXT,
                resident_cnt TEXT
            )
            DISTRIBUTED BY (id)
        ''')
        logging.warning('CREATE TABLE')

        pg_hook.run(f'TRUNCATE TABLE {self.table_name}', False)
        logging.warning('TRUNCATE TABLE')

        for data in self.result:
            pg_hook.run(f'''
                INSERT INTO {self.table_name} (id, name, type, dimension, resident_cnt)
                VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')
            ''')
        logging.warning('INSERT VALUES')


class DmikuzminRamLocationsOperator(BaseOperator):
    """
    Класс для поиска топ 3 локации
    """

    ui_color = "#7071A1"

    def __init__(self, api_url: str, table_name: str, **kwargs) -> None:
        """
        Функция инициализации
        :param api_url: Ссылка на API
        :param table_name: таблица в БД
        :param kwargs: прочие параметры
        """
        super().__init__(**kwargs)
        self.api_url = api_url
        self.table_name = table_name

    def parse_result(self, loc):
        """
        Функция для распарсивания результата
        :param loc: имя локации
        :return: список параметров этой локации
        """
        id_ = loc['id']
        name = loc['name']
        type_ = loc['type']
        dimension = loc['dimension']
        resident_cnt = len(loc['residents'])
        return [id_, name, type_, dimension, resident_cnt]

    def execute(self, context):  # Метод execute
        """
        Для каждой страницы происходит парсинг, данные складываются в список result
        :param context:
        :return:
        """
        result = []
        next_page = self.api_url
        while next_page:
            r = requests.get(next_page)
            if r.status_code == 200:
                response = r.json()
                for loc in response['results']:
                    result.append(self.parse_result(loc))
                next_page = response['info']['next']
            else:
                logging.warning("HTTP STATUS {}".format(r.status_code))
                raise AirflowException('Error in load page count')

        result.sort(key=lambda x: x[4], reverse=True)  # Сортировка по count resident_cnt
        top_result = result[:3]  # Limit 3 results
        logging.warning(f"Result:\n{top_result}")


        # Создаю ЭК моего Hook
        posgreshook = DmikuzminRickMortyHook(result=top_result, table_name=self.table_name)
        posgreshook.insert_gp()
