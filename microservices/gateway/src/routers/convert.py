from urllib.parse import urlparse
from fastapi import Depends, APIRouter, UploadFile, Request
from src.utils.httpx import httpx_client_wrapper
from config import (
    API_MAX_REQUESTS_PER_DAY, API_SECONDS_IN_DAY, 
    SERVER_JPG_HOST, SERVER_JPG_PORT, 
    SERVER_PNG_HOST, SERVER_PNG_PORT, 
    SERVER_WEBP_HOST, SERVER_WEBP_PORT)
from fastapi_limiter.depends import RateLimiter

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=str, dependencies=[Depends(RateLimiter(times=API_MAX_REQUESTS_PER_DAY, seconds=int(API_SECONDS_IN_DAY)))], status_code=201)
async def convert_to_jpg(image: UploadFile, request: Request):
    outbound_url = "http://{}:{}{}".format(
        SERVER_JPG_HOST, SERVER_JPG_PORT,
        urlparse(str(request.url)).path)
    async_client = httpx_client_wrapper()
    file = {'image': (image.filename, image.file, image.content_type)}
    res = await async_client.post(outbound_url, files=file)
    result = res.text.replace("\"","")
    return result

@convert_router.post('/to-png', response_model=str, dependencies=[Depends(RateLimiter(times=API_MAX_REQUESTS_PER_DAY, seconds=int(API_SECONDS_IN_DAY)))], status_code=201)
async def convert_to_png(image: UploadFile, request: Request):
    outbound_url = "http://{}:{}{}".format(
        SERVER_PNG_HOST, SERVER_PNG_PORT,
        urlparse(str(request.url)).path)
    async_client = httpx_client_wrapper()
    file = {'image': (image.filename, image.file, image.content_type)}
    res = await async_client.post(outbound_url, files=file)
    result = res.text.replace("\"","")
    return result

@convert_router.post('/to-webp', response_model=str, dependencies=[Depends(RateLimiter(times=API_MAX_REQUESTS_PER_DAY, seconds=int(API_SECONDS_IN_DAY)))], status_code=201)
async def convert_to_webp(image: UploadFile, request: Request):
    outbound_url = "http://{}:{}{}".format(
        SERVER_WEBP_HOST, SERVER_WEBP_PORT,
        urlparse(str(request.url)).path)
    async_client = httpx_client_wrapper()
    file = {'image': (image.filename, image.file, image.content_type)}
    res = await async_client.post(outbound_url, files=file)
    result = res.text.replace("\"","")
    return result