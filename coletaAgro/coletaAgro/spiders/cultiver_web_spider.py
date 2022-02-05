'''
# N=10 em: https://sistemas.agricultura.gov.br/snpc/cultivarweb/detalhe_cultivar.php?codsr=N
Os campos a serem extraídos e salvos no banco são:
Cultivar
Nome Comum
Nome Científico
Situação
Nº Registro
Data do Registro
Mantenedor (Requerente)
'''
from datetime import datetime, date
import json

import scrapy
import re
import psycopg2
from ..items import CultivarItem


def get_shell_base():
    return {"cultivar": "",
            "nome_comum": "",
            "nome_cientifico": "",
            "situacao": "",
            "num_registro": "",
            "data_registro": "",
            "requerente": ""
            }


def get_shell_base():
    return ["cultivar", "nome_comum",
            "nome_cientifico",
            "situacao",
            "num_registro",
            "data_registro",
            "requerente"
            ]


class QuotesSpider(scrapy.Spider):
    name = "crawler_cultivar"

    @staticmethod
    def base_url_generator(n):
        return f'https://sistemas.agricultura.gov.br/snpc/cultivarweb/detalhe_cultivar.php?codsr={n}'

    def start_requests(self):
        for n in range(1, 11):  # 11
            yield scrapy.Request(url=self.base_url_generator(n), callback=self.parse)

    def parse(self, response):
        info_table = response.css('tr.td_resultado123').css('td::text').extract()[:7]
        result = [re.sub(pattern=r'\r*|\t*|\n*|\\*', repl='', string=re.escape(answer))
                  for answer in info_table]

        '''
        page = response.url.split("=")[-1]
        filename = f'cultivar-page-{page}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({"data": result}, f, indent=4, ensure_ascii=False)
        self.log(f'Saved file {filename}')
        '''
        item = dict(zip(get_shell_base(), result))
        item['data_registro'] = convert_str_to_date(item['data_registro'])

        yield CultivarItem(item)


def convert_str_to_date(value: str) -> date:
    return datetime.strptime(value, '%d/%m/%Y')
