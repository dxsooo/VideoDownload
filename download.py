import argparse
import os
import time
import traceback

import yt_dlp

DOWNLOAD_DIR = "./Downloads"

ydl_opts = {
    "format": "best",
    "outtmpl": "",
    "external_downloader": "aria2c",
    "external_downloader_args": ["-x16", "-c"],
    "merge_output_format": "mp4",
}


def download_youtube(url, ydl):
    for retry in range(3):
        try:
            ydl.download([url])
            break
        except Exception as e:
            traceback.print_exc()
            print("retry in 2 seconds")
            time.sleep(2)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="video playing url")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    ydl_opts["outtmpl"] = os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        download_youtube(args.url, ydl)
