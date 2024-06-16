# Earthfile for building and testing the lark-escaping project
FROM python:3.11

# Install Poetry
build:
    RUN pip install poetry
    COPY pyproject.toml poetry.lock ./
    RUN poetry install
    SAVE ARTIFACT . AS LOCAL ./

# Run tests using pytest
test:
    FROM +build
    COPY . .
    RUN poetry run pytest
