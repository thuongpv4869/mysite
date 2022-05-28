FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements /code/requirements

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements/local.txt