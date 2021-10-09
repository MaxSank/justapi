import ast
from datetime import datetime
import yaml
from mysql.connector import Error
from django.core.management.base import BaseCommand
from main.management.commands.module import do_connection


select_querie = """SELECT name, time, number, text, list
                FROM main_record"""


"""Connect and select data from MySQL DB"""


def select_from_mysql(sql_command):
    connection = None
    cursor = None
    result = []
    try:
        connection = do_connection()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            print(result)
            connection.commit()
            print(f'Command: {sql_command}\nResult: successfully')
    except Error as e:
        print("Error while connecting to MySQL: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Connection is closed')
            return result


"""Literal evaluate list"""


def prepare_data(data_from_db):
    for element in data_from_db:
        new_list = ast.literal_eval(element['list'])
        element['list'] = new_list
    return data_from_db


"""Write data from MySQL to another yaml file"""


def write_to_new_yaml(prepared_list):
    with open('data2.yaml', 'w') as file:
        yaml.dump(prepared_list, file, default_flow_style=False)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = select_from_mysql(select_querie)
        data = prepare_data(data)
        write_to_new_yaml(data)
