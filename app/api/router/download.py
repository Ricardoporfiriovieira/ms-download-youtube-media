from fastapi import APIRouter, HTTPException
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError
from fastapi import HTTPException, Query
from fastapi.responses import FileResponse
from os import path, rename

router = APIRouter()


@router.post("/download")
async def download_video(
    url: str = Query(..., description="YouTube video URL"),
    format: str = Query(..., description="Download format: mp4 or mp3"),
):

    if format not in ["mp4", "mp3"]:
        raise HTTPException(
            status_code=400, detail="Invalid format. choose 'mp4' or 'mp3'."
        )

    try:
        yt = YouTube(url)
    except RegexMatchError:
        raise HTTPException(status_code=400, detail="Invalid URL")
    except AgeRestrictedError:
        raise HTTPException(status_code=403, detail="Age restriction error")

    file_path = download_single_video(url, format)
    if not file_path:
        raise HTTPException(status_code=500, detail="Erro: could not dowload video")

    return FileResponse(
        path=file_path,
        filename=path.basename(file_path),
        media_type="application/octet-stream",
    )


def download_single_video(link: str, format: str):
    yt = YouTube(link)
    if format == "mp4":
        video = yt.streams.get_highest_resolution()
        file_path = video.download()
        new_file_path = path.splitext(file_path)[0] + "_video.mp4"
        rename(file_path, new_file_path)
    elif format == "mp3":
        audio = yt.streams.filter(only_audio=True).first()
        file_path = audio.download()
        new_file_path = path.splitext(file_path)[0] + ".mp3"
        rename(file_path, new_file_path)
    return new_file_path
