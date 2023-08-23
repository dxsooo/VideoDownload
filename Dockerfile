FROM python:3.11-alpine as poetry

WORKDIR /root

# install poetry
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock ./
RUN poetry export -E celery -o requirements.txt

# app
FROM python:3.11-slim

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends aria2 ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=poetry /root/requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY *.py ./

ENTRYPOINT [ "python" ]