from typing import Optional, List
import logging
import os
import environ
import mysql.connector
from mysql.connector import Error


def do_connection():
    """Connect with MySQL DB"""
    environ.Env.read_env()
    host = os.environ.get('MySQL_host')
    database = os.environ.get('MySQL_database')
    user = os.environ.get('MYSQL_user')
    password = os.environ.get('MySQL_password')

    connection = mysql.connector.connect(
        host=f'{host}',
        database=f'{database}',
        user=f'{user}',
        password=f'{password}'
    )
    return connection


def execute_sql_queries(single_or_many, sql_query, take_give_ot_not, data_to_insert=None) -> Optional[List[tuple]]:
    """Connect, execute queries, close connection
    'single' = cursor.execute()
    'many' = cursor.executemany()
    'data' = insert/update data
    'no data' = default value of data_to_insert
    'fetchall' = fetch all data from db, default value of data_to_insert"""
    logging.basicConfig(level=logging.INFO)
    connection = None
    cursor = None
    information = None

    try:
        connection = do_connection()

        if connection.is_connected():

            cursor = connection.cursor()

            if single_or_many == 'single' and take_give_ot_not == 'data':
                cursor.execute(sql_query, data_to_insert)
            elif single_or_many == 'single' and take_give_ot_not == 'no data':
                cursor.execute(sql_query)
            elif single_or_many == 'many':
                cursor.executemany(sql_query, data_to_insert)
            elif take_give_ot_not == 'fetchall':
                cursor.execute(sql_query)
                information = cursor.fetchall()

                information = information.copy()
                logging.info(information)

            connection.commit()
            logging.info(f'Command: {sql_query}\nResult: successfully')

    except Error as e:
        logging.error("Error while connecting to MySQL: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logging.info('Connection is closed')
            return information
