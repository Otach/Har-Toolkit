#!/usr/bin/env python3
from urllib.parse import urlparse


class VideoEntry:
    """A class to represent a video from the HAR file."""

    def __init__(self, entry):
        self.entry = entry
        self.url = urlparse(self.entry.request.url)
        self.filename = self.url.path.split("/")[-1]
        self.entry.response.content.decode()
        self.video_data = self.entry.response.content.text

    def save(self, dir=".", filename=None):
        if filename is None:
            filename = self.filename

        path = f"{dir}/{filename}"
        with open(path, "wb") as video_output:
            video_output.write(self.video_data)

    def __str__(self):
        return f"{self.filename}"
