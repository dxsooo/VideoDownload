import argparse

from config import DOWNLOAD_DIR
from download_bilibili import download_bilibili_video, is_bilibili_video
from download_youtube import download_youtube_video, is_youtube_video


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="video playing url")
    parser.add_argument(
        "-d", "--dir", default=DOWNLOAD_DIR, help="video save directory"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    dir = args.dir
    url = args.url

    if is_youtube_video(url):
        download_youtube_video(url, dir)
    elif is_bilibili_video(url):
        download_bilibili_video(url, dir)
    else:
        print("Invalid video url")
