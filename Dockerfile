ARG PYTHON_VERSION=3.8.3

FROM python:${PYTHON_VERSION}-alpine

ENV POETRY_HOME="/etc/poetry" \
    POETRY_VIRTUALENVS_CREATE="false"

ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN echo $PATH

RUN apk update && \
    apk add libpq && \
    apk add --virtual .build-deps curl gcc python3-dev musl-dev postgresql-dev && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    mkdir /code

RUN echo ${PATH}

WORKDIR /code

COPY . .

RUN poetry install --no-dev

RUN apk del .build-deps
