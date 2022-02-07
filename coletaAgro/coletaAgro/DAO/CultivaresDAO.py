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
        return f'postgresql://{self.username}:{self.password}@{self.hostname}:{self.database_port}/{self.database_name}?connect_timeout=10&application_name={self.app_name}'

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
                return False
        else:
            print('query finalizada')
            return True

    def close_connection(self):
        try:
            self.connection.close()
            return True
        except OperationalError as e:
            print(e)
            return False
