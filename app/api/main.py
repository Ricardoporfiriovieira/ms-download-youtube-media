from fastapi import APIRouter

from app.api.router import youtube_downloader

api_router = APIRouter()
api_router.include_router(youtube_downloader.router, tags=["youtube_downloader"])