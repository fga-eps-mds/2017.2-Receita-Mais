# Trabalho de GCS - 2017.2 - Receituário médico.
[![Build Status](https://travis-ci.org/fga-gpp-mds/2017.2-Receituario-Medico.svg?branch=master)](https://travis-ci.org/fga-gpp-mds/2017.2-Receituario-Medico)
[![Coverage Status](https://coveralls.io/repos/github/fga-gpp-mds/2017.2-Receituario-Medico/badge.svg)](https://coveralls.io/github/fga-gpp-mds/2017.2-Receituario-Medico)
[![Code Climate](https://codeclimate.com/github/fga-gpp-mds/2017.2-Receituario-Medico/badges/gpa.svg)](https://codeclimate.com/github/fga-gpp-mds/2017.2-Receituario-Medico)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<p align="center"><img src="https://raw.githubusercontent.com/wiki/fga-gpp-mds/2017.2-Receituario-Medico/imagens/logo/logo.png" width="350px"></p>

<p align="justify">O Receituário Médico é um sistema direcionado para os profissionais de saúde que é idealizado pelo médico Getúlio de Morato Filho com o objetivo de tornar a prescrição médica mais rápida e fácil. E o outro viés que o sistema atende é o aproximar o contato do paciente com o médico através de um portal onde será possível visualizar suas receitas e tirar eventuais dúvidas sobre elas.</p>

<p align="justify">O principal objetivo do projeto é poder facilitar a prescrição de receitas por médicos aos seus pacientes fazendo assim com que o médico use melhor o tempo da consulta. O médico passa grande parte de uma consulta prescrevendo os medicamentos em folha ou até mesmo digitando no sistema. A solução proposta agirá justamente nesse ponto para minimizar o tempo com que uma receita é prescrita.</p>

## Integrantes
|               Aluno              |           Matrícula           |
|:---------------------------------:|:-------------------------:|
|      Ronyell Henrique dos Santos      |  15/0046073 |
|      Thiago Nogueira Freire           |  15/0047142 |

## Integração Contínua
- A integração contínua do projeto se deu através da ferramenta Travis. A escolha da ferramenta se deu por a dupla possuir maior afinidade com a mesmsa e o por a ferramenta atender todas as necessidades do projeto.
- Link para informações da build: https://travis-ci.org/fga-gpp-mds/2017.2-Receituario-Medico

## Isolamento do Ambiente

A ferramenta de isolamento de ambiente foi utilizado o Docker. O ambiente ficou divido em dois containers, sendo um container a aplicação e outro container o banco de dados. O Docker-Comopose oi utilizado ara realizar o provisionamento entre os containers possibilitando assim a comunicação entre eles. Para iniciar os containers é necessário executar o comando a baixo.
```python
docker-compose up
```
O docker também é utilizado na ferramenta Travis, pois o mesmo é inicializado para executar os testes e verificar se estão todos corretos. Foi adotado subir o docker para o Travis para que o ambiente de desenvolvimento e o ambiente de testes possuissem as mesmas características. 


## Automação do Ambiente

A ferramenta utilizada para realizar automação do ambiente foi a ferramenta Ansible. A maioria das configurações iniciais do ambiente se dão através do Dockefile e do doceker-compose.yml, devido a importância dessas ferramentas as mesmas foram adicionadas para serem instaladas através do playbook.yml. É necessário possuir instalado o Ansible localmente e possuir a pasta /etc/ansible/hosts com um arquivo de hosts apontando para o ip local 127.0.0.1. Para executar a instalação tanto do Docker quanto do Docker-Compose é necessário executar o seguinte comando:

```python
ansible-playbook playbook.yml
```

## Build
A build foi realizada através do Gulp para que fosse possível realizar o sincronísmo do HTML, CSS e JS com o servidor da plicação. Para visualizar a aplicação sincronizada é necessário entrar na porta 3000 e não na 8000 default do Django. Os comandos para realizar a inicialização do Gulp foram adicionados ao Dockerfile, por isso não é necessário realizar nenhum comando no terminal para executar o Gulp.

## Empacotamento
O projeto foi empacotado para a extensão .egg com o auxilio da ferramenta setuptools que possibilita pegar todas as dependências e criar o empacotamento .egg. A aplicação é empacotada e colocada em uma pasta chamada ReceitaMais.egg-info onde possuis os arquivos que foram gerados pelo processo de empacotamento através da ferramenta setuptools. O comando para realizar o empacotamento da aplicação é: 

```python
python3 setup.py bdist_egg
```


## Deploy
A ferramenta que foi utilizada para a realização do Deploy contínuo foi o Heroku. A aplicação pode ser acessada através do seguinte link: [https://preskribe.herokuapp.com/](https://preskribe.herokuapp.com/)
