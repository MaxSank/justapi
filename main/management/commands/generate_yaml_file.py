from typing import List
import requests
from bs4 import BeautifulSoup
import random
import datetime
import yaml
from django.core.management.base import BaseCommand


def get_names() -> List[str]:
    """Get names for Records"""
    r = requests.get('https://en.wikipedia.org/wiki/List_of_culinary_fruits')
    soup = BeautifulSoup(r.text, features="html.parser")
    table = soup.findAll('tbody')[0].findAll('a')[3:]

    """BS tag.string returns NavigableString, not str"""
    names_list = [str(element.string) for element in table]
    return names_list


def create_list(lst_of_names: List[str]) -> List[dict]:
    """Create list for writing in YAML-file"""
    final_list = []
    for element in lst_of_names:
        dct = {
            'name': element,
            'time': datetime.datetime(
                2020,
                1,
                1,
                random.randint(0, 23),
                random.randint(0, 59),
                0
            ),
            'number': round(random.uniform(0, 10), 2),
            'text': (str(element) + ' ') * 5,
            'list': [random.randint(0, 20) for _ in range(10)]
        }
        final_list.append(dct)
    return final_list


def write_to_yaml(prepared_lst: List[dict]) -> None:
    """Write data to YAML-file"""
    with open('data.yaml', 'w') as file:
        yaml.dump(prepared_lst, file, default_flow_style=False)


class Command(BaseCommand):

    def handle(self, *args, **options):
        names = get_names()
        fin_list = create_list(names)
        write_to_yaml(fin_list)
