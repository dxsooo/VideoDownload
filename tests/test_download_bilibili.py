import hashlib
import os

import pytest

from download_bilibili import download_bilibili_video, is_bilibili_video


class TestDownloadBilibili:
    test_dl_dir = "test_dl"

    def test_is_bilibili_video(self):
        tests = ["https://www.bilibili.com/video/BV1NF411P7C9"]
        for t in tests:
            assert is_bilibili_video(t)

    def test_is_not_bilibili_video(self):
        tests = ["https://www.bilibili.com/video/1be4y1X7sq"]
        for t in tests:
            assert not is_bilibili_video(t)

    def test_download_bilibili_video(self):
        download_bilibili_video(
            "https://www.bilibili.com/video/BV1NF411P7C9", self.test_dl_dir
        )
        fn = os.path.join(self.test_dl_dir, "BV1NF411P7C9.mp4")
        assert os.path.exists(fn)
        assert 49233582 <= os.path.getsize(fn) <= 49233583

    def test_download_bilibili_video_failures(self):
        with pytest.raises(Exception):
            download_bilibili_video(
                "https://www.bilibili.com/video/BV1Ur4y1G7en", self.test_dl_dir
            )
