import os
import re

from you_get import common


def is_ixigua_video(url: str) -> bool:
    return None != re.match("^https://www.ixigua.com/[0-9]+$", url)


def download_ixigua_video(url: str, dir: str):
    os.makedirs(dir, exist_ok=True)
    common.skip_existing_file_size_check = True
    common.output_filename = get_id(url)
    # print(common.output_filename)
    common.any_download(url=url, info_only=False, output_dir=dir, merge=True)


def get_id(url: str) -> str:
    se = re.search(r"([0-9]+)$", url)
    if se != None:
        return se.group(0)
