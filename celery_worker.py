from dotenv import find_dotenv, load_dotenv

# load env parameters from file named .env
load_dotenv(find_dotenv())

import os

from celery import Celery

from download_bilibili import download_bilibili_video, is_bilibili_video
from download_youtube import download_youtube_video, is_youtube_video

app = Celery(
    "VideoDownload",
    broker=os.getenv("BROKER"),
    backend=os.getenv("BACKEND"),
)


@app.task
def download(url: str):
    if is_youtube_video(url):
        download_youtube_video(url)
    elif is_bilibili_video(url):
        download_bilibili_video(url)
    else:
        return None
