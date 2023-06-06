FROM python:3.11-slim-bullseye

# poetry
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends aria2 ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# app
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --extras celery

COPY *.py ./

ENTRYPOINT [ "python" ]