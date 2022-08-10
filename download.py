import argparse
import os

from config import DOWNLOAD_DIR
from download_bilibili import download_bilibili_video, is_bilibili_video
from download_youtube import download_youtube_video, is_youtube_video


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="video playing url")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    url = args.url
    if is_youtube_video(url):
        download_youtube_video(url)
    elif is_bilibili_video(url):
        download_bilibili_video(url)
    else:
        print("Invalid video url")
