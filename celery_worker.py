from dotenv import find_dotenv, load_dotenv

# load env parameters from file named .env
load_dotenv(find_dotenv())

import os

from celery import Celery

from config import DOWNLOAD_DIR
from download import download

app = Celery(
    "VideoDownload",
    broker=os.getenv("BROKER"),
    backend=os.getenv("BACKEND"),
)


@app.task
def download(url: str, dir: str = DOWNLOAD_DIR):
    download(url, dir)
    return {"source": url}
