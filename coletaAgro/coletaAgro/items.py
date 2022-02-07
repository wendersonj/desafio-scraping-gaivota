# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from .DAO.CultivaresDAO import CultivaresDB


class CultivarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cultivar = scrapy.Field()
    nome_comum = scrapy.Field()
    nome_cientifico = scrapy.Field()
    situacao = scrapy.Field()
    num_registro = scrapy.Field()
    data_registro = scrapy.Field()
    requerente = scrapy.Field()

    @staticmethod
    def insert_data(db: CultivaresDB, sql_data):
        sql = ("""insert into cultivar(cultivar, nome_comum, nome_cientifico, situacao,
                num_registro, data_registro, requerente) values(%s, %s, %s, %s, %s, %s, %s)""")
        return db.query(sql, sql_data)

    @staticmethod
    def get_all(db):
        db.cursor.execute('select * from cultivar')
        return db.cursor.fetchall()

    @staticmethod
    def print_all(db):
        results = CultivarItem.get_all(db)
        for rec in results:
            print(rec)
