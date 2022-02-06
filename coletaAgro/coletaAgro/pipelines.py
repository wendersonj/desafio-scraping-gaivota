# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .DAO.CultivaresDAO import CultivaresDB
from .items import CultivarItem
from .utils.utils import convert_str_to_date


class CultivarPipeline:
    db = CultivaresDB()

    def open_spider(self, spider):
        self.db.create_connection()

    def close_spider(self, spider):
        self.db.close_connection()

    def process_item(self, item: CultivarItem, spider):
        item['data_registro'] = convert_str_to_date(item['data_registro'])

        CultivarItem.insert_data(db=self.db, sql_data=[item['cultivar'], item['nome_comum'],
                                                       item['nome_cientifico'], item['situacao'],
                                                       item['num_registro'], item['data_registro'],
                                                       item['requerente']])

        return item
