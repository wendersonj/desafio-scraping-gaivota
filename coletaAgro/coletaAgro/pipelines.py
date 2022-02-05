# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .items import CultivarItem
from .utils.utils import convert_str_to_date


class CultivarPipeline:

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item: CultivarItem, spider):
        item.data_registro = convert_str_to_date(item.data_registro)

        return item
