import asyncio
import glob
import os
import re
from pathlib import Path
from typing import Optional

import bilix.sites.bilibili.api as api
from bilix.sites.bilibili.downloader import DownloaderBilibili


def is_bilibili_video(url: str) -> bool:
    if None != re.match(r"^https://www.bilibili.com/video/BV[a-zA-z0-9]+$", url):
        return True
    else:
        return None != re.match(r"^http://www.bilibili.com/video/av[0-9]+$", url)


def download_bilibili_video(url: str, dir: str):
    os.makedirs(dir, exist_ok=True)
    asyncio.run(
        _download_video(url, DownloaderBilibili(part_concurrency=10), videos_dir=dir)
    )


def get_id(url: str) -> Optional[str]:
    se = re.search(r"(BV[a-zA-z0-9]+)$", url)
    if se != None:
        return se.group(0)

    se = re.search(r"(av[0-9]+)$", url)
    if se != None:
        return se.group(0)

    return None


async def _download_video(url: str, bdl: DownloaderBilibili, videos_dir: str):
    # get bvid/avid from url to rename later
    name = get_id(url)
    if name is None:
        raise Exception(f"Failed to get video id in {url}")

    try:
        # hack video info to set name
        video_info = await api.get_video_info(bdl.client, url)
        # print(video_info.pages[video_info.p].p_name)
        video_info.pages[video_info.p].p_name = name

        await bdl.get_video(url, path=Path(videos_dir), video_info=video_info)
        out_vs = glob.glob(os.path.join(videos_dir, "*-" + name + ".mp4"))
        if len(out_vs) == 0:
            raise Exception(f"Failed to get video in {url}")
        os.rename(
            out_vs[0],
            os.path.join(videos_dir, name + ".mp4"),
        )
    except Exception:
        # clean
        out_vs = glob.glob(os.path.join(videos_dir, "*-" + name + "*"))
        for o in out_vs:
            os.remove(o)
        raise
    finally:
        await bdl.aclose()
