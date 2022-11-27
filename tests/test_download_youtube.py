import hashlib
import os

import pytest

from download_youtube import download_youtube_video, is_youtube_video


class TestDownloadYoutube:
    test_dl_dir = "test_dl"

    def test_is_youtube_video(self):
        tests = ["https://www.youtube.com/watch?v=_wO522Dgtrk"]
        for t in tests:
            assert is_youtube_video(t)

    def test_is_not_youtube_video(self):
        tests = ["https://www.youtube.com/watch"]
        for t in tests:
            assert not is_youtube_video(t)

    def test_download_youtube_video(self):
        download_youtube_video(
            "https://www.youtube.com/watch?v=_wO522Dgtrk", self.test_dl_dir
        )
        fn = os.path.join(self.test_dl_dir, "_wO522Dgtrk.mp4")
        assert os.path.exists(fn)
        with open(fn, "rb") as file_to_check:
            data = file_to_check.read()
            assert hashlib.md5(data).hexdigest() == "fa3986677b1220fc9de5972bf1998574"

    def test_download_youtube_video_failures(self):
        with pytest.raises(Exception):
            download_youtube_video(
                "https://www.youtube.com/watch?v=pBxN2GjY_08", self.test_dl_dir
            )
