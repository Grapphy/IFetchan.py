import aiohttp

from typing import List

BASEPOST = "https://a.4cdn.org"
BASECDN = "https://i.4cdn.org"


class FourchanImage:
    __slots__ = (
        "filename",
        "thumbnail_url",
        "full_url",
    )

    def __init__(
        self, *, filename: str, thumbnail_url: str, full_url: str
    ) -> None:
        self.filename = filename
        self.thumbnail_url = thumbnail_url
        self.full_url = full_url

    def __repr__(self) -> str:
        return (
            f"fname={self.filename} thumb={self.thumbnail_url}"
            f" full={self.full_url}"
        )


async def get_thread_pictures(
    board: str, thread_id: str
) -> List[FourchanImage]:
    images: List[FourchanImage] = []
    url = f"{BASEPOST}/{board}/thread/{thread_id}.json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.headers["Content-Type"] == "application/json":
                rjson = await res.json()
            else:
                return images

    for thread in rjson["posts"]:
        if "ext" in thread:
            fname = str(thread["tim"]) + thread["ext"]
            thumb_url = f"{BASECDN}/{board}/{thread['tim']}s.jpg"
            full_url = f"{BASECDN}/{board}/{fname}"
            fobj = FourchanImage(
                filename=fname, thumbnail_url=thumb_url, full_url=full_url
            )
            images.append(fobj)

    return images


async def get_bytes_from_url(url: str) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            return await res.read()
