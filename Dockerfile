FROM python:3.10-slim-bullseye

# poetry
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
ENV PATH="/root/.local/bin:$PATH"

RUN apt-get -qq update && \
    apt-get install -qqy aria2 ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --extras celery

WORKDIR /app
COPY *.py ./

ENTRYPOINT [ "python" ]