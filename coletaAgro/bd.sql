create database cultivares;

create table cultivar(
id serial primary key,
	cultivar varchar(255) not null,
nome_comum varchar(255) not null,
nome_cientifico varchar(255) not null,
situacao varchar(255) not null,
num_registro varchar(50),
data_registro date not null,
requerente varchar(500)
);