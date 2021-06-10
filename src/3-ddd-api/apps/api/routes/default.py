import pathlib
import json

from fastapi import APIRouter

router = APIRouter()

TAG = "default"


@router.get("/", tags=[TAG])
async def index():
    """Index of application"""
    return dict(application="Training API")


@router.get("/health", tags=[TAG])
async def health():
    """Readyness probe endpoint"""
    return dict(healthy=True)