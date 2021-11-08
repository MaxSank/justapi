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


def execute_sql_queries(single_or_many, sql_querie, take_give_ot_not, data_to_insert=None):
    """Connect, execute queries, close connection
    'single' = cursor.execute()
    'many' = cursor.executemany()
    'data' = insert/update data
    'no data' = default value of data_to_insert
    'fetchall' = fetch all data from db, default value of data_to_insert"""
    connection = None
    cursor = None
    information = None

    try:
        connection = do_connection()

        if connection.is_connected():

            cursor = connection.cursor()

            if single_or_many == 'single' and take_give_ot_not == 'data':
                cursor.execute(sql_querie, data_to_insert)
            elif single_or_many == 'single' and take_give_ot_not == 'no data':
                cursor.execute(sql_querie)
            elif single_or_many == 'many':
                cursor.executemany(sql_querie, data_to_insert)
            elif take_give_ot_not == 'fetchall':
                cursor.execute(sql_querie)
                information = cursor.fetchall()

                information = information.copy()
                print(information)

            connection.commit()
            print(f'Command: {sql_querie}\nResult: successfully')

    except Error as e:
        print("Error while connecting to MySQL: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Connection is closed')
            return information
