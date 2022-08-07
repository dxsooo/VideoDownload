# VideoDownload

VideoDownload tool for *Youtube/BiliBili* using Aria2

## Usage

Requirements:

- Aria2
- Python 3
- Poetry(as package management)

Setup(for normal users):

```bash
poetry export -f requirements.txt | pip install -r /dev/stdin
```

Run:

```bash
python download.py <VideoURL>
```

VideoURL is the video playing url.  
For Youtube, it should be <https://www.youtube.com/watch?v=xxx>  
For BiliBili, it should be <https://www.bilibili.com/video/xxxx>

The video is saved in `Downloads/` of the current path.

### With Docker

## Develop

It is welcome to make PR. After cloning, You can start with:

```bash
poetry install
```

Browse the code freely.
