# VideoDownload

VideoDownload tool for *Youtube/BiliBili*

## Usage

### With source code

Requirements:

- Aria2(for youtube)
- FFmpeg(for bilibili)
- Poetry(as package management)
- Python 3.8+

Setup(for normal users, developers refer [Contributing](#Contributing)):

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
For BiliBili, it should be <https://www.bilibili.com/video/BVxxxx>

The video is saved in `videos/` of the current path and named with video id.

### With Docker

You can easily download video by docker:

```bash
docker run -t -v/path/to/save:/app/Downloads dxsooo/video-download:0.1.0 download.py -u <VideoURL>
```

> v0.1.0 save video to `./Downloads`

## Celery worker mode

VideoDownload can also work as a Celery worker that receive download jobs. It is recommended to use by docker:

```bash
docker run -d --name video-downloader-1 \
    -eBROKER= \
    -eRESULT_URL= \
    -v/path/to/save:/app/videos \
    dxsooo/video-download:0.2.0 celery_worker.py
```

And then you can send job by one of the following methods:

### 1.use RabbitMQ admin page

Supposing RabbitMQ is used as BROKER, you can send job on its admin page after login:

### 2.use

For all brokers, it is a general method

## Contributing

It is welcome to make PR. After cloning, You can start with:

```bash
poetry install
source`poetry env info --path`/bin/activate
```

For Youtube, [YT-DLP](https://github.com/yt-dlp/yt-dlp) is used with aria2 as external downloader. For BiliBili, [Bilix](https://github.com/HFrost0/bilix) is used.

If you need to work with Celery mode, you can start with:

```bash
poetry install
```

And there are scripts(docker compose is needed) in `./devenv` that help to create local environment for broker(RabbitMQ) and result storage(MongoDB):

```bash
cd devenv
./setup.sh
```

> Edit .env file if you want to use external broker or storage

Run the worker with:

```bash
python celery_worker.py
```

In addition to the methods described in [Celery worker mode](#Celery-worker-mode), you can send jobs by:

```bash
python send_celery_job.py
```

## Thanks

- [Bilix](https://github.com/HFrost0/bilix)
- [YT-DLP](https://github.com/yt-dlp/yt-dlp)
