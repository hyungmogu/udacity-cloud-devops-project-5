import logging
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile

from src.models.convert import ConvertedImage
from src.services.convert import ImgToJPGService, ImgToPNGService, ImgToWEBPService

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=ConvertedImage, status_code=201)
async def convert_to_jpg(image: UploadFile):
    logging.debug(f"file: {image}")
    
    service = ImgToJPGService()
    in_mem_file = service.convert_to_jpg(image)
    result = service.upload_file(in_mem_file, 'jpg')
    return result

@convert_router.post('/to-png', response_model=ConvertedImage, status_code=201)
async def convert_to_png(file: UploadFile):
    service = ImgToPNGService()
    in_mem_file = service.convert_to_png(file)
    result = service.upload_file(in_mem_file, 'png')
    return result

@convert_router.post('/to-webp', response_model=ConvertedImage, status_code=201)
async def convert_to_webp(file: UploadFile):
    service = ImgToWEBPService()
    in_mem_file = service.convert_to_webp(file)
    result = service.upload_file(in_mem_file, 'webp')
    return result
