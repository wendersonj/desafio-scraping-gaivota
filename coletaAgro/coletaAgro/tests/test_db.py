from datetime import date
from itertools import zip_longest

from psycopg2 import OperationalError

from ..DAO.CultivaresDAO import CultivaresDB
from ..items import CultivarItem
from ..spiders.cultiver_web_spider import get_shell_base

'''
use pytest
'''


def test_db_connection():
    db = CultivaresDB()
    try:
        cursor = db.create_connection()
    except OperationalError:
        assert False

    assert cursor is not None


def test_insert_item_in_db():
    db = CultivaresDB()
    db.create_connection()
    item = ['Arroz', 'Arrozinho',
            'Arroz de verdade',
            'regular', '8002',
            date(9999, 1, 1),
            'wenderson']

    item = dict(zip_longest(get_shell_base(), item))

    result = CultivarItem.insert_data(db=db, sql_data=[item['cultivar'], item['nome_comum'],
                                                       item['nome_cientifico'], item['situacao'],
                                                       item['num_registro'], item['data_registro'],
                                                       item['requerente']])
    assert result
