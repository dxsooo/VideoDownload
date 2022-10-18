# VideoDownload

[![GitHub](https://img.shields.io/github/license/dxsooo/VideoDownload)](./LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/dxsooo/VideoDownload?display_name=tag)](https://github.com/dxsooo/VideoDownload/releases/latest)
[![CodeFactor](https://www.codefactor.io/repository/github/dxsooo/videodownload/badge)](https://www.codefactor.io/repository/github/dxsooo/videodownload)
[![Docker Pulls](https://img.shields.io/docker/pulls/dxsooo/video-download?logo=docker)](https://hub.docker.com/repository/docker/dxsooo/video-download)
<!-- [![GitHub all releases](https://img.shields.io/github/downloads/dxsooo/VideoDownload/total)]((https://github.com/dxsooo/VideoDownload/releases/latest)) -->

VideoDownload tool for *Youtube/BiliBili/douyin*

## Usage

### Standalone mode

#### With source code

Requirements:

- Aria2 (for Youtube)
- FFmpeg (for Youtube、BiliBili)
- Poetry (as package management)
- Python 3.8+

Setup (for normal users, developers refer [Contributing](#Contributing)):

```bash
git clone https://github.com/dxsooo/VideoDownload.git
cd VideoDownload
poetry export -f requirements.txt | pip install -r /dev/stdin
```

Run:

```bash
python download.py -u <VideoURL>
```

VideoURL is the video playing url.  
For Youtube, it should be <https://www.youtube.com/watch?v=xxx>  
For BiliBili, it should be <https://www.bilibili.com/video/BVxxxx> or <http://www.bilibili.com/video/avxxxx>  
For douyin, it should be <https://www.douyin.com/video/xxxx>

The video is saved in `videos/` of the current path and named with video id.

There are more options:

```bash
% python download.py --help
usage: download.py [-h] -u URL [-d DIR]

options:
  -h, --help         show this help message and exit
  -u URL, --url URL  video playing url
  -d DIR, --dir DIR  video save directory
```

#### With Docker

You can easily download video by docker:

```bash
docker run -t -v/path/to/save:/app/videos dxsooo/video-download:0.2.7 download.py -u <VideoURL>
```

### Celery worker mode

VideoDownload can also work as a [Celery](https://docs.celeryq.dev/en/stable/index.html) worker that receive download tasks, making it possible and convenient to deploy in distribute systems and integrate with cloud-native services.

It is recommended to use by docker:

```bash
docker run -d --name video-downloader-1 \
    -e BROKER=${YOUR_CELERY_BROKER} \
    -e BACKEND=${YOUR_CELERY_BACKEND} \
    -v /path/to/save:/app/videos \
    --entrypoint=celery \
    dxsooo/video-download:0.2.7 -A celery_worker worker -c 4
```

> For BiliBili, as some deps could not run with multi process, concurrency(-c) should be 1. But it is ok to run multi docker containers to walk around.

And then you can send task by one of the following methods:

#### 1.with Celery, Python only

```python
# pip install celery
from celery import Celery
celery = Celery(broker="<YOUR_CELERY_BROKER>")
celery.send_task('celery_worker.download',("<VideoURL>",))
```

#### 2.use REST API from celery flower, language-independent

Start flower by:

```bash
docker run -d --name video-downloader-flower \
    -e BROKER=${YOUR_CELERY_BROKER} \
    -e BACKEND=${YOUR_CELERY_BACKEND} \
    --entrypoint=celery \
    -p 5555:5555 \
    dxsooo/video-download:0.2.7 -A celery_worker flower
```

Example request:

```http
POST /api/task/async-apply/celery_worker.download HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate, compress
Content-Type: application/json; charset=utf-8
Host: localhost:5555

{
    "args": ["<VideoURL>"]
}
```

> if you want to use custom queue instead of the default `celery`, start worker with `-Q <queue>`, and send request refer <https://github.com/mher/flower/issues/456>

## Additional Configuration

As [YT-DLP](https://github.com/yt-dlp/yt-dlp) is used in youtube download, a method to config its options is provided. You can add an ini file in `configs/youtube.ini` with content like:

```ini
[ydl_opts]
max_filesize=314572800 ; limit file size, 300M
```

> You can also mount the ini file to docker container for configuration.

## Contributing

It is welcome to make PR. After cloning, You can start with:

```bash
poetry install
source`poetry env info --path`/bin/activate
```

Different deps is used for different sources:

|source|deps|
|-|-|
|Youtube|[YT-DLP](https://github.com/yt-dlp/yt-dlp) + aria2(as external downloader)|
|BiliBili|[Bilix](https://github.com/HFrost0/bilix)|
|douyin|[You-Get](https://github.com/soimort/you-get)|

The main concern are download speed and the ability of integration.

If you need to work with Celery mode, you can start with:

```bash
poetry install -E celery
```

And there are scripts(docker compose is needed) in `./devenv` that help to create local environment for broker(RabbitMQ) and result backend(MongoDB):

```bash
cd devenv
./start.sh
```

> Create/edit `.env` file if you want to use external broker or backend

Run the worker with:

```bash
celery -A celery_worker worker
```

Start flower(<http://localhost:5555>) with:

```bash
celery -A celery_worker flower
```

In addition to the methods described in [Celery worker mode](#Celery-worker-mode), you can send tasks by:

```bash
python send_celery_task.py
```

## Thanks

- [Bilix](https://github.com/HFrost0/bilix)
- [YT-DLP](https://github.com/yt-dlp/yt-dlp)
- [You-Get](https://github.com/soimort/you-get)
