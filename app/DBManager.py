
from typing import Optional

import psycopg
from dotenv import load_dotenv
from loguru import logger
from psycopg import connect

from singleton import SingletonMeta
from settings import POSTGRES_NAME, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT


class DBManager(metaclass=SingletonMeta):
    def __init__(self, env_file='../.env'):
        load_dotenv(env_file)
        self.db_name = POSTGRES_NAME
        self.db_user = POSTGRES_USER
        self.db_password = POSTGRES_PASSWORD
        self.db_host = POSTGRES_HOST
        self.db_port = POSTGRES_PORT
        self.conn_str = None
        self.set_conn_str()
        self.conn = None
        self.conn = self.connect()

    def set_conn_str(self) -> None:
        self.conn_str = f"dbname={self.db_name} user={self.db_user} password={self.db_password} host={self.db_host} port={self.db_port}"
        logger.info(f'Setting connection string {self.conn_str}')

    def connect(self) -> psycopg.Connection:
        try:
            self.conn = connect(self.conn_str)
            return self.conn
        except psycopg.Error as e:
            logger.error(f'Database error: {e}')

    def execute_query(self, query: str) -> None:
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    conn.commit()
        except psycopg.Error as e:
            logger.error(f'Database error: {e}')

    def execute_fetch_query(self, query: str, n: int = None) -> Optional[list]:
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    if not n:
                        return cursor.fetchall()
                    return cursor.fetchmany(n)
        except psycopg.Error as e:
            logger.error(f'Database error: {e}')

    def init_tables(self):
        self.execute_query(open('init_tables.sql', 'r').read())

    def close(self):
        self.conn.close()
        self.conn = None
