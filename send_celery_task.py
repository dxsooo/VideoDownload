from celery_worker import download

test_urls = [
    # "https://www.youtube.com/watch?v=sHFsq-BIhWs",
    "https://www.bilibili.com/video/BV1be4y1X7sq",
    "https://www.bilibili.com/video/BV1NF411P7C9",
    "https://github.com",
]

if __name__ == "__main__":
    for i in test_urls:
        download.delay(i)
