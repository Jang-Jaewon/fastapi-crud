FROM python:3.10.12-slim

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
COPY app /app/app

RUN apt-get update -y && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev \
    && apt-get remove curl -y \
