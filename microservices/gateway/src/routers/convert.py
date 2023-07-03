from io import BytesIO
import logging
from fastapi import APIRouter, HTTPException, status, UploadFile
from src.utils.httpx import httpx_client_wrapper

from src.services.convert import ImgToJPGService, ImgToPNGService, ImgToWEBPService

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=str, status_code=201)
async def convert_to_jpg(image: UploadFile, url: str = None):
    # @TODO: Add code that checks for rate limit

    async_client = httpx_client_wrapper()
    res = await async_client.post(url, files={'file': image.file})
    result = res.text
    return {
        'result': result,
        'status': res.status_code
    }

@convert_router.post('/to-png', response_model=str, status_code=201)
async def convert_to_png(image: UploadFile, url: str = None):
    # @TODO: Add code that checks for rate limit

    async_client = httpx_client_wrapper()
    res = await async_client.post(url, files={'file': image.file})
    result = res.text
    return {
        'result': result,
        'status': res.status_code
    }

@convert_router.post('/to-webp', response_model=str, status_code=201)
async def convert_to_webp(image: UploadFile, url: str = None):
    # @TODO: Add code that checks for rate limit

    async_client = httpx_client_wrapper()
    res = await async_client.post(url, files={'file': image.file})
    result = res.text
    return {
        'result': result,
        'status': res.status_code
    }