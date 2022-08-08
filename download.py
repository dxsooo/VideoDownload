import argparse
import asyncio
import glob
import os
import re
import time
import traceback

import bilix
import yt_dlp

DOWNLOAD_DIR = "./Downloads"

re_pattern = {
    "Youtube": "^https:\/\/www.youtube.com\/watch\?v=[a-zA-z0-9\-]+$",
    "BiliBili": "^https:\/\/www.bilibili.com\/video\/BV[a-zA-z0-9]+$",
}

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


async def download_bilibili(url, bdl):
    # get bvid from url to rename later
    name = re.search(r"BV([a-zA-z0-9]+)$", url).group(1)
    co = bdl.get_video(url, add_name=name)
    await asyncio.gather(co)
    os.rename(
        glob.glob(os.path.join(bdl.videos_dir, "*-" + name + ".mp4"))[0],
        os.path.join(bdl.videos_dir, name + ".mp4"),
    )
    await bdl.aclose()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="video playing url")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    if re.match(re_pattern["Youtube"], args.url):
        ydl_opts["outtmpl"] = os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            download_youtube(args.url, ydl)
    elif re.match(re_pattern["BiliBili"], args.url):
        asyncio.run(
            download_bilibili(
                args.url, bilix.Downloader(part_concurrency=10, videos_dir=DOWNLOAD_DIR)
            )
        )
    else:
        print("Invalid video url")
