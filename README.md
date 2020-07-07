# Flask-commerce

[![pipeline status](https://gitlab.com/rcristiano/flask-commerce/badges/master/pipeline.svg)](https://gitlab.com/rcristiano/flask-commerce/commits/master)  [![coverage report](https://gitlab.com/rcristiano/flask-commerce/badges/master/coverage.svg)](https://gitlab.com/rcristiano/flask-commerce/-/commits/master)


A simple REST API for e-commerce made with Flask

## Pipeline and versioning

This project uses as a base the project **[semver_ci](https://gitlab.com/rcristiano/semver_ci)** for pipeline and versioning.

## Running

### With Docker

#### Requirements

- Docker: ^19.03.12
- Docker compose: ^1.22.0

#### Starting application

Run `docker-compose up -d` to start all services.

#### Tests

To run tests, you have to access the *flask* service. This can be done using the following command:

```sh
docker-compose exec flask sh
/code# poetry install
/code# coverage run -m unittest discover tests/
```

### Local

#### Requirements:

- Python: 3.8.3
- pyenv: ^1.2.19-3
- Poetry: ^1.0.9
- PostgreSQL: 12.3

> `poetry` was used for package management and `pyenv` was used for python versions management.

#### Starting application

> Change necessary variables in `.env` to connect with your `PostgreSQL` server


With `poetry` and `pyenv` installed, install python 3.8.3 with pyenv:

`pyenv install 3.8.3`

Then start the app with:

```sh
export $(cat .env | xargs)
export DEV_DATABASE_URL="${DB_ENGINE}://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_URL}:${POSTGRES_PORT}/${POSTGRES_DB}"
poetry install
flask run -h '0.0.0.0' -p 80
```

## Flasgger - Swagger endpoints documentation

With application runing access http://localhost/apidocs/

## Heroku

https://flask-commerce.herokuapp.com/

## TODO

- [x] Endpoints documentation
  - [x] Flasgger ?
- [x] Cart manager
- [ ] Implement schema validation with Cerberus
- [ ] Improve authentication security with JWT / OAuth2
