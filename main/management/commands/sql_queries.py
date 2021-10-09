from django.core.management.base import BaseCommand
from main.management.commands.module import execute_sql_queries


"""MySQL commands:"""

create_table = """CREATE TABLE test (
                id INT PRIMARY KEY AUTO_INCREMENT,
                fr_name TEXT,
                value FLOAT NOT NULL,
                string TEXT
                );"""

# No AUTO_INCREMENT in id =  Duplicate entry '0' for key 'PRIMARY'
insert_select = """INSERT INTO test (fr_name, value, string)
                SELECT name, number, text FROM main_record
                WHERE number < 8 AND id NOT IN (1, 10)
                ORDER BY number;"""

update_table = """UPDATE test SET
                value = 1,
                string = fr_name
                WHERE value < 5;"""

delete_rows = """DELETE FROM test ORDER BY value DESC LIMIT 1;"""

join_tables = """SELECT test.fr_name, main_record.list AS list_from_main
                FROM test JOIN main_record
                ON test.fr_name = main_record.name;"""

create_view = """CREATE VIEW test2 AS
                SELECT name, list FROM main_record;"""

select_view = """SELECT * FROM test2"""

drop_view = """DROP VIEW test2"""

drop_table = """DROP TABLE test"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        execute_sql_queries('single', create_table, 'no data')
        execute_sql_queries('single', insert_select, 'no data')
        execute_sql_queries('single', update_table, 'no data')
        execute_sql_queries('single', delete_rows, 'no data')
        execute_sql_queries('single', join_tables, 'fetchall')
        execute_sql_queries('single', create_view, 'no data')
        execute_sql_queries('single', select_view, 'fetchall')
        execute_sql_queries('single', drop_view, 'no data')
        execute_sql_queries('single', drop_table, 'no data')
