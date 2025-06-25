# dioapi




<h1>Desafio final de projeto: api python</h1>

# MARCELO BARUDI
 

 
 Uma breve descrição sobre minhas qualificações
 
 Engenharia Civil, Faculdade de Engenharia São Paulo - (Dez/1997).
 MBA Gestão Empresarial – Pós-Graduação UNIP (2010).
 Engenharia de Segurança do Trabalho - Pós-Graduação USP/PECE (2014).
 Técnicas de Transações Imobiliárias – INED (2018).
 Analista de Cibersegurança Júnior- CISCO(2024)
 
 
 
 Minha redes sociais:
 
 [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/marcelo-barudi) 
 [![E-mail](https://img.shields.io/badge/-Email-0077B5?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:marcelobarudi71@gmail.com)
 [![WhatsApp](https://img.shields.io/badge/WhatsApp-0077B5?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5511985919330)
 [![GitHub](https://img.shields.io/badge/GitHub-0077B5?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MBARUDI)
 
 ## About me 
 
 Eu estou estudando as linguagens de programação. :+1:
 
 | Rank | Languages |
 |-----:|-----------|
 | 1| JavaScript|
 | 2| Python |
 | 3| SQL |
 | 4| Java |
 
 - Criação de sites
 
 1. [x] https://github.com/MBARUDI/maximobrasilmanut.git
 
 ##✨ **HABILIDADES E COMPETÊNCIAS:**
 
 1. Engenharia civil
 2. Segurança do Trabalho
 3. Gestão empresarial
 4. Programação
 5. Análise de dados


### Quem é o FastAPi?
Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção.
FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async
Código assíncrono apenas significa que a linguagem tem um jeito de dizer para o computador / programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar

# Projeto
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER
![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Execução da API

Para executar o projeto, utilizei a [pyenv](https://github.com/pyenv/pyenv), com a versão 3.11.4 do `python` para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
```
Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
make run-docker
```
Para criar uma migration nova, execute:

```bash
make create-migrations d="nome_da_migration"
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs


# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/