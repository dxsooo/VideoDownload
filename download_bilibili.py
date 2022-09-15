import asyncio
import glob
import os
import re

import bilix


def is_bilibili_video(url: str) -> bool:
    if None != re.match("^https:\/\/www.bilibili.com\/video\/BV[a-zA-z0-9]+$", url):
        return True
    else:
        return None != re.match("^http:\/\/www.bilibili.com\/video\/av[0-9]+$", url)


def download_bilibili_video(url: str, dir: str):
    os.makedirs(dir, exist_ok=True)
    asyncio.run(
        download_bilibili(
            url, bilix.DownloaderBilibili(part_concurrency=10, videos_dir=dir)
        )
    )


def get_id(url: str) -> str:
    se = re.search(r"(BV[a-zA-z0-9]+)$", url)
    if se != None:
        return se.group(0)
    else:
        return re.search(r"(av[0-9]+)$", url).group(0)


async def download_bilibili(url, bdl):
    # get bvid/avid from url to rename later
    name = get_id(url)
    try:
        await bdl.get_video(url, add_name=name)
        out_vs = glob.glob(os.path.join(bdl.videos_dir, "*-" + name + ".mp4"))
        if len(out_vs) == 0:
            raise Exception(f"Failed to get video in {url}")
        os.rename(
            out_vs[0],
            os.path.join(bdl.videos_dir, name + ".mp4"),
        )
    except:
        # clean
        out_vs = glob.glob(os.path.join(bdl.videos_dir, "*-" + name + "*"))
        for o in out_vs:
            os.remove(o)
        raise
    finally:
        await bdl.aclose()
