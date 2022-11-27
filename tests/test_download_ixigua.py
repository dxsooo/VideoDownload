import hashlib
import os

import pytest

from download_ixigua import download_ixigua_video, is_ixigua_video

# from download_douyin import download_duoyin_video, is_douyin_video


class TestDownloadIxigua:
    test_dl_dir = "test_dl"

    def test_is_ixigua_video(self):
        tests = ["https://www.ixigua.com/7170354202705658420"]
        for t in tests:
            assert is_ixigua_video(t)

    def test_is_not_ixigua_video(self):
        tests = ["https://www.ixigua.com/video/1be4y1X7sq"]
        for t in tests:
            assert not is_ixigua_video(t)

    def test_download_ixigua_video(self):
        download_ixigua_video(
            "https://www.ixigua.com/7170354202705658420", self.test_dl_dir
        )
        fn = os.path.join(self.test_dl_dir, "7170354202705658420.mp4")
        assert os.path.exists(fn)
        with open(fn, "rb") as file_to_check:
            data = file_to_check.read()
            assert hashlib.md5(data).hexdigest() == "8f6f3eb0bfe716f144cd1ec48df915dc"

    def test_download_ixigua_video_failures(self):
        with pytest.raises(Exception):
            download_ixigua_video(
                "https://www.ixigua.com/video/BV1Ur4y1G7en", self.test_dl_dir
            )
