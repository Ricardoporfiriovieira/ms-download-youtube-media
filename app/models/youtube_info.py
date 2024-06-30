from pydantic import BaseModel


class YoutubeInfo(BaseModel):
    title: str
    image: str
