from fastapi import APIRouter

from app.api.router import download, info

api_router = APIRouter()
api_router.include_router(download.router, tags=["download"])
api_router.include_router(info.router, tags=["info"])
