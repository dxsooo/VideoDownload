import configparser
import os
import re

import yt_dlp

from config import YOUTUBE_CONFIG_PATH

ydl_opts = {
    "format": "best",
    "outtmpl": "",
    "external_downloader": "aria2c",
    "external_downloader_args": ["-x16", "-c", "--file-allocation=none"],
    "merge_output_format": "mp4",
    "writesubtitles": True,
    "subtitleslangs": ["zh.*"],
    "postprocessors": [
        {  # Embed subtitle in video using ffmpeg.
            "key": "FFmpegEmbedSubtitle",
            "already_have_subtitle": False,
        }
    ],
}

if os.path.exists(YOUTUBE_CONFIG_PATH):
    config = configparser.ConfigParser()
    config.read(YOUTUBE_CONFIG_PATH)
    ydl_opts.update(config["ydl_opts"])
    if "max_filesize" in ydl_opts.keys() and ydl_opts["max_filesize"] != "":
        ydl_opts["max_filesize"] = int(ydl_opts["max_filesize"])
        del ydl_opts["external_downloader"]
        del ydl_opts["external_downloader_args"]


def is_youtube_video(url: str) -> bool:
    return None != re.match(
        "^https:\/\/www.youtube.com\/watch\?v=[A-Za-z0-9_\-]+$", url
    )


def download_youtube_video(url: str, dir: str):
    os.makedirs(dir, exist_ok=True)
    ydl_opts["outtmpl"] = os.path.join(dir, "%(id)s.%(ext)s")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
