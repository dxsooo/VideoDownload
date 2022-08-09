import asyncio
import glob
import os
import re

import bilix

from config import DOWNLOAD_DIR


def is_bilibili_video(url: str) -> bool:
    return None != re.match("^https:\/\/www.bilibili.com\/video\/BV[a-zA-z0-9]+$", url)


def download_bilibili_video(url: str):
    asyncio.run(
        download_bilibili(
            url, bilix.Downloader(part_concurrency=10, videos_dir=DOWNLOAD_DIR)
        )
    )


async def download_bilibili(url, bdl):
    # get bvid from url to rename later
    name = re.search(r"(BV[a-zA-z0-9]+)$", url).group(0)
    co = bdl.get_video(url, add_name=name)
    await asyncio.gather(co)
    os.rename(
        glob.glob(os.path.join(bdl.videos_dir, "*-" + name + ".mp4"))[0],
        os.path.join(bdl.videos_dir, name + ".mp4"),
    )
    await bdl.aclose()
