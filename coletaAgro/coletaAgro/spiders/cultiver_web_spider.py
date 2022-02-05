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

import re

import scrapy

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

        yield CultivarItem(dict(zip(get_shell_base(), result)))
