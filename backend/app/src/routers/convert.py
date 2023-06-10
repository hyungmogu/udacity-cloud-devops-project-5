from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status

from src.database.connections import get_session
from src.services.convert import ImgToJPGService


convert_router = APIRouter(
    tags=["Convert"]
)


@convert_router.post('/jpg', response_model=ConvertedImage, status_code=201)
async def convert_to_jpg(file: UploadFile):
    service = ImgToJPGService()
    in_mem_file = service.convert_to_jpg(file)
    result = service.upload_file(in_mem_file, 'jpg')
    return result

@convert_router.post('/png', response_model=ConvertedImage, status_code=201)
async def convert_to_png(file: UploadFile) -> ConvertedImage:
    service:ConvertServices = ConvertServices()
    result:ConvertedImage = service.convert_to_png(file)
    return result

@convert_router.post('/webp', response_model=ConvertedImage, status_code=201)
async def convert_to_webp(file: UploadFile) -> ConvertedImage:
    service:ConvertServices = ConvertServices()
    result:ConvertedImage = service.convert_to_webp(file)
    return result
