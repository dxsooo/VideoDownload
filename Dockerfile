FROM python:3.10-slim-bullseye

# poetry
RUN pip config set global.trusted-host mirrors.aliyun.com && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
ADD https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py get-poetry.py 
RUN python get-poetry.py
ENV PATH="/root/.poetry/bin:$PATH"

RUN apt-get -qq update && \
    apt-get install -qqy aria2 ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# app
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --extras celery -f requirements.txt | pip install -r /dev/stdin

WORKDIR /app
COPY *.py ./

ENTRYPOINT [ "python" ]