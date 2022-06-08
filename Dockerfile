FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="$PATH:/root/.poetry/bin"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /code/

RUN --mount=type=cache,target=/root/.cache/poetry poetry install --no-interaction --no-ansi