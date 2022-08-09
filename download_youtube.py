import os
import re
import time
import traceback

import yt_dlp

from config import DOWNLOAD_DIR

ydl_opts = {
    "format": "best",
    "outtmpl": "",
    "external_downloader": "aria2c",
    "external_downloader_args": ["-x16", "-c"],
    "merge_output_format": "mp4",
}


def is_youtube_video(url: str) -> bool:
    return None != re.match("^https:\/\/www.youtube.com\/watch\?v=[a-zA-z0-9\-]+$", url)


def download_youtube_video(url: str):
    ydl_opts["outtmpl"] = os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        download_youtube(url, ydl)


def download_youtube(url, ydl):
    for retry in range(3):
        try:
            ydl.download([url])
            break
        except Exception as e:
            traceback.print_exc()
            print("retry in 2 seconds")
            time.sleep(2)
