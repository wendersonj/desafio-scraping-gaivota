# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


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
