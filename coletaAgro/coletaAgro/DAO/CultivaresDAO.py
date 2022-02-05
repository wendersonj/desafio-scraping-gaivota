import datetime

import psycopg2
from psycopg2._psycopg import OperationalError
from psycopg2.errorcodes import NOT_NULL_VIOLATION


class CultivaresDB:
    hostname = 'localhost'
    database_port = '5432'
    username = 'postgres'
    password = '123456'
    database_name = 'cultivares'
    app_name = 'coletaAgro'

    @property
    def get_database_uri(self):
        return f'postgresql://{self.username}:{self.password}@{self.hostname}:{self.database_port}/{self.database_name}?connect_timeout=10&application_name={app_name}'

    connection = None

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(host=CultivaresDB.hostname, database=CultivaresDB.database_name,
                                               user=CultivaresDB.username, password=CultivaresDB.password)
        except OperationalError as e:
            print(f'nao foi possivel conectar. error: {e}')
            raise e
        else:
            return self.connection.cursor()

    @property
    def cursor(self):
        return self.connection.cursor()

    def query(self, query_sql, sql_data):
        try:
            self.cursor.execute(query_sql, sql_data)
            self.connection.commit()
        except psycopg2.errors.NotNullViolation as e:
            if e.pgcode == NOT_NULL_VIOLATION:
                print('Erro:', e)
        else:
            print('query finalizada')

    def get_all(self):
        self.cursor.execute('select * from cultivar')
        return self.cursor.fetchall()

    def print_all(self):
        recset = self.get_all()
        for rec in recset:
            print(rec)

    def close_connection(self):
        try:
            self.connection.close()
        except OperationalError as e:
            print(e)


if __name__ == '__main__':
    sql = """insert into cultivar(cultivar, nome_comum, nome_cientifico, situacao,
					 num_registro, data_registro, requerente) values('Arroz', 'Arrozinho',
																	 'Arroz de verdade', 
																	 'regular', '8002', 
																	 '2023-01-01',
																	'wenderson')"""

    sql = ''
    sql_data = ['Arroz', 'Arrozinho',
                'Arroz de verdade',
                'regular', '8002',
                datetime.date(9999, 1, 1),
                'wenderson']
