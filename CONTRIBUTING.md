# Welcome to contributing guide

## Get Started

```bash
poetry install
source`poetry env info --path`/bin/activate
```

> You had better know about **poetry**

Different deps is used for different sources:

|source|deps|
|-|-|
|Youtube|[YT-DLP](https://github.com/yt-dlp/yt-dlp) + aria2(as external downloader)|
|BiliBili|[Bilix](https://github.com/HFrost0/bilix)|
|douyin|[You-Get](https://github.com/soimort/you-get)|

The main concern are download speed and the ability of integration.

You are free to adjust the download_*.py files for your demand and make PRs.

## Celery Mode

If you need to work with Celery mode, you should:

```bash
poetry install -E celery
```

### Local Environment

There are scripts (docker compose is needed) in `./devenv` that help to create local environment for broker(RabbitMQ) and result backend(MongoDB):

```bash
cd devenv
./start.sh
```

> Create/edit `.env` file if you want to use external broker or backend

Run the worker with:

```bash
celery -A celery_worker worker
```

Start flower in <http://localhost:5555> with:

```bash
celery -A celery_worker flower
```

In addition to the methods described in [Celery Mode](./README.md#celery-mode), you can send tasks by:

```bash
python send_celery_task.py
```

### Monitoring

Follow the instructions in [Monitoring](./monitoring/README.md)
