import os
import re

from you_get import common


def is_douyin_video(url: str) -> bool:
    return None != re.match("^https:\/\/www.douyin.com\/video\/[0-9]+$", url)


def download_douyin_video(url: str, dir: str):
    os.makedirs(dir, exist_ok=True)
    common.output_filename = get_id(url)
    common.any_download(
        url=url, stream_id="mp4", info_only=False, output_dir=dir, merge=True
    )


def get_id(url: str) -> str:
    se = re.search(r"([0-9]+)$", url)
    if se != None:
        return se.group(0)
