# Desafio Scraping - Gaivota

# Configurando o banco de dados (Postgres)

Execute o script de *query* localizado na pasta  `desafio-scraping-gaivota/coletaAgro/bd.sql`

# Como usar - Localmente:

0- Vá para a pasta do projeto e abra a pasta da aplicação
```
$ cd desafio-scraping-gaivota
```

1-Instalação do ambiente virtual

```
$ pip install virtualenv
```

2-Criar um novo ambiente virtual

```
$ virtualenv venv
```

3-Ativar o ambiente virtual

```
$ .\env\Scripts\activate
```

4-Instalar as dependências

```
$ pip install -r requirements.txt
```

5-Mova o terminal para a pasta da aplicação

```
$ cd coletaAgro
```


6-Executar a aplicação

```
$ scrapy crawl crawler_cultivar
```
