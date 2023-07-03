from io import BytesIO
import logging
from fastapi import APIRouter, HTTPException, status, UploadFile

from src.services.convert import ImgToJPGService, ImgToPNGService, ImgToWEBPService

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=str, status_code=201)
async def convert_to_jpg(image: UploadFile):
    pass

@convert_router.post('/to-png', response_model=str, status_code=201)
async def convert_to_png(image: UploadFile):
    pass

@convert_router.post('/to-webp', response_model=str, status_code=201)
async def convert_to_webp(image: UploadFile):
    pass