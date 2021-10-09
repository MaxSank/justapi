import random
import yaml
from django.core.management.base import BaseCommand
from main.management.commands.module import execute_sql_queries


"""MySQL command for insert data to DB"""


mysql_command = """INSERT INTO main_record
                (name, time, number, text, list)
                VALUES (%(name)s, %(time)s, %(number)s, %(text)s, %(list)s);
                """


"""Load data from yaml-file"""


def read_yaml_file():
    with open('data.yaml', 'r') as file:
        """calling yaml.load() without Loader=... is deprecated,
        as the default Loader is unsafe."""
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


"""Processing lists inside elements (dicts) of data,
sort and delete minimal and maximal numbers in lists."""


def processing_list(data_list):
    for element in data_list:
        for parts in element:
            if isinstance(element[parts], list):
                element[parts].sort()
                element[parts].pop(0)
                element[parts].pop()

                element.update({'list': str(element[parts])})


"""Processing numbers"""


def processing_numbers(data_list):
    for element in data_list:
        for parts in element:
            if isinstance(element[parts], float):
                element[parts] = str(round(element[parts] + 1, 2))


"""Delete space in the end of text"""


def processing_text(data_list):
    for element in data_list:
        element['text'] = element['text'].rstrip()


"""Change month in datetime"""


def processing_datetime(data_list):
    for element in data_list:
        element['time'] = element['time'].replace(month=random.randint(1, 12))
        element['time'] = element['time'].strftime('%Y-%m-%d %H:%M:%S')


"""Management command"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_from_file = read_yaml_file()
        processing_list(data_from_file)
        processing_numbers(data_from_file)
        processing_text(data_from_file)
        processing_datetime(data_from_file)

        # Insert data with def from module
        execute_sql_queries('many', mysql_command, 'data', data_from_file)
