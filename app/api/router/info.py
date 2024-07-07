from fastapi import APIRouter, HTTPException
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError
from fastapi import HTTPException, Query
from app.models.youtube_info import YoutubeInfo

router = APIRouter()


@router.get("/info")
async def get_video_info(url: str = Query(..., description="Youtube video URL")):
    try:
        yt = YouTube(url)
    except RegexMatchError:
        raise HTTPException(status_code=400, detail="invalid URL")
    except AgeRestrictedError:
        raise HTTPException(status_code=403, detail="Age restriction error")

    return YoutubeInfo(title=yt.title, image=yt.thumbnail_url, url=url)
