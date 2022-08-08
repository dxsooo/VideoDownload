# VideoDownload

VideoDownload tool for *Youtube/BiliBili*

## Usage

### With source code

Requirements:

- Aria2(for youtube)
- Python 3.8+
- Poetry(as package management)

Setup(for normal users):

```bash
poetry export -f requirements.txt | pip install -r /dev/stdin
```

Run:

```bash
python download.py -u <VideoURL>
```

VideoURL is the video playing url.  
For Youtube, it should be <https://www.youtube.com/watch?v=xxx>  
For BiliBili, it should be <https://www.bilibili.com/video/BVxxxx>

The video is saved in `Downloads/` of the current path.

### With Docker

TODO

## Celery worker mode

TODO

## Contributing

It is welcome to make PR. After cloning, You can start with:

```bash
poetry install
source`poetry env info --path`/bin/activate
```

Browse the code freely with your IDE.

For Youtube, [YT-DLP](https://github.com/yt-dlp/yt-dlp) is used with aria2 as external downloader. For BiliBili, [Bilix](https://github.com/HFrost0/bilix) is used.

## Thanks

- [Bilix](https://github.com/HFrost0/bilix)
- [YT-DLP](https://github.com/yt-dlp/yt-dlp)
