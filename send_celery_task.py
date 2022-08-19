from celery_worker import download
from config import DOWNLOAD_DIR

test_urls = [
    # "https://www.youtube.com/watch?v=sHFsq-BIhWs",
    "https://www.bilibili.com/video/BV1be4y1X7sq",
    "https://www.bilibili.com/video/BV1NF411P7C9",
    "https://www.bilibili.com/video/BV1Ur4y1G7en",  # 失效视频
]

if __name__ == "__main__":
    for i in test_urls:
        download.delay(i, DOWNLOAD_DIR)
        # download.delay(i)
        # download.apply_async((i, DOWNLOAD_DIR), queue="bilibili")
