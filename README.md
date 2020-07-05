# Flask-commerce

[![pipeline status](https://gitlab.com/rcristiano/flask-commerce/badges/master/pipeline.svg)](https://gitlab.com/rcristiano/flask-commerce/commits/master)  [![coverage report](https://gitlab.com/rcristiano/flask-commerce/badges/master/coverage.svg)](https://gitlab.com/rcristiano/flask-commerce/-/commits/master)


A simple REST API for e-commerce made with Flask

## Pipeline and versioning

This project uses as a base the project **[semver_ci](https://gitlab.com/rcristiano/semver_ci)** for pipeline and versioning.

## Requirements

### With docker:

- Docker: ^19.03.12
- Docker compose: ^1.22.0

### For run in your machine:

- Python: 3.8.3
- pyenv: ^1.2.19-3
- Poetry: ^1.0.9
- PostgreSQL: 12.3

> For python package management `poetry` was used and for python versions `pyenv` was used, together `poetry` manages virtualenvs

## Pyenv

## How to run

### With Docker

run: `docker-compose up -d`

> To run tests access **sh** from `flask` service:

run: 
```sh
docker-compose exec flask sh
/code# poetry install
/code# coverage run -m unittest discover tests/
```

### Locally

> Change necessary variables in `.env` to connect with your `PostgreSQL` server


With `poetry` and `pyenv` installed, install python version `pyenv install 3.8.3` on project folder run:
```sh
export $(cat .env | xargs)
export DEV_DATABASE_URL="${DB_ENGINE}://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_URL}:${POSTGRES_PORT}/${POSTGRES_DB}"
poetry install
flask run -h '0.0.0.0' -p 80
```

## TODO

- [ ] Endpoints documentation
  - [ ] Flasgger ?
- [x] Cart manager
