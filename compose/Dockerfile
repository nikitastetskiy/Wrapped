FROM python:3.8 AS compile-image

RUN pip install poetry

workdir /app
COPY . ./

RUN poetry install
RUN poetry run python -m pytest
