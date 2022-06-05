FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY Pipfile /code
COPY Pipfile.lock /code

RUN --mount=type=cache,target=/root/.cache/pip pip install pipenv

RUN virtualenv /venv
ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/pipenv pipenv install --dev -v