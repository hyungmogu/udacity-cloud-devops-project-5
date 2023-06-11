from io import BytesIO
import logging
from fastapi import APIRouter, HTTPException, status, UploadFile

from src.models.convert import ConvertedImage
from src.services.convert import ImgToJPGService, ImgToPNGService, ImgToWEBPService

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=ConvertedImage, status_code=201)
async def convert_to_jpg(image: UploadFile):
    try:
        image_binary = await image.read()
        buffer = BytesIO(image_binary)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_420_ENHANCE_YOUR_CALM, detail="Error converting image.")

    service = ImgToJPGService()
    in_mem_file = service.convert(buffer)
    result = service.upload(in_mem_file, 'jpg')
    
    return result

@convert_router.post('/to-png', response_model=ConvertedImage, status_code=201)
async def convert_to_png(image: UploadFile):
    try:
        image_binary = await image.read()
        buffer = BytesIO(image_binary)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_420_ENHANCE_YOUR_CALM, detail="Error converting image.")

    service = ImgToPNGService()
    in_mem_file = service.convert(buffer)
    result = service.upload(in_mem_file, 'png')
    return result

@convert_router.post('/to-webp', response_model=ConvertedImage, status_code=201)
async def convert_to_webp(image: UploadFile):
    try:
        image_binary = await image.read()
        buffer = BytesIO(image_binary)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_420_ENHANCE_YOUR_CALM, detail="Error converting image.")
    
    service = ImgToWEBPService()
    in_mem_file = service.convert(buffer)
    result = service.upload(in_mem_file, 'webp')
    return result
