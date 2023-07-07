from io import BytesIO
import logging
from fastapi import APIRouter, HTTPException, status, UploadFile

from src.services.convert import ImgToJPGService

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=str, status_code=201)
async def convert_to_jpg(image: UploadFile):

    if image is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No image provided.")

    if (image.content_type != 'image/jpeg' and
        image.content_type != 'image/jpg' and
        image.content_type != 'image/png' and 
        image.content_type != 'image/webp'):
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Only png, jpg, jpeg, webp images are supported.")

    try:
        image_binary = await image.read()
        buffer = BytesIO(image_binary)
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_420_ENHANCE_YOUR_CALM, detail="Error converting image.")

    service = ImgToJPGService()
    in_mem_file = service.convert(buffer)
    result = service.upload(in_mem_file, 'jpg')

    if result is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error uploading image.")

    return result