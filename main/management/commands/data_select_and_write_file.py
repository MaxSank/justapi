from typing import List
import logging
from datetime import datetime
import yaml
from mysql.connector import Error
from django.core.management.base import BaseCommand
from main.management.commands.module import do_connection


def select_from_mysql(sql_command: str) -> List[dict]:
    """Connect and select data from MySQL DB"""
    connection = None
    cursor = None
    result = []
    try:
        connection = do_connection()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            logging.info(result)
            connection.commit()
            logging.info(f'Command: {sql_command}\nResult: successfully')
    except Error as e:
        logging.error("Error while connecting to MySQL: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logging.info('Connection is closed')
            return result


def prepare_data(data_from_db: List[dict]) -> List[dict]:
    """Parse string, convert to list type"""
    for element in data_from_db:
        new_list = [int(el) for el in element['list'].lstrip('[').rstrip(']').split(', ')]
        element['list'] = new_list
    return data_from_db


def write_to_new_yaml(prepared_list: List[dict]) -> None:
    """Write data from MySQL to another yaml file"""
    with open('data2.yaml', 'w') as file:
        yaml.dump(prepared_list, file, default_flow_style=False)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)
        select_query = """SELECT name, time, number, text, list
                        FROM main_record"""

        data = select_from_mysql(select_query)
        data = prepare_data(data)
        write_to_new_yaml(data)
