import time

from dotenv import find_dotenv, load_dotenv

# load env parameters from file named .env
load_dotenv(find_dotenv())

import os

from celery import Celery

from config import DOWNLOAD_DIR
from download import download as _download

app = Celery(
    "VideoDownload",
    broker=os.getenv("BROKER"),
    backend=os.getenv("BACKEND"),
)


@app.task
def download(
    url: str, dir: str = DOWNLOAD_DIR, hold_on_sec: int = 0, base_spend_sec: int = 0
):
    t0 = time.time()
    _download(url, dir)
    wt = base_spend_sec - (time.time() - t0)
    if wt > 0:
        time.sleep(wt)
    # set hold on time to make task longer, that avoid abusing target website
    time.sleep(hold_on_sec)
    return {"source": url}
