from typing import Any
from urllib.parse import urlparse
from fastapi import APIRouter, UploadFile, Request, HTTPException
from src.utils.httpx import httpx_client_wrapper
from src.utils.rate_limiter import rate_limiter
from src.utils.ip_address import to_ip_address
from config import (
    API_MAX_REQUESTS_PER_DAY,
    SERVER_JPG_HOST, SERVER_JPG_PORT,
    SERVER_PNG_HOST, SERVER_PNG_PORT,
    SERVER_WEBP_HOST, SERVER_WEBP_PORT)

convert_router = APIRouter(
    tags=["Convert"]
)

@convert_router.post('/to-jpg', response_model=str, status_code=201)
@rate_limiter(API_MAX_REQUESTS_PER_DAY)
async def convert_to_jpg(image: UploadFile, request: Request) -> Any:
    outbound_url = "http://{}:{}{}".format(
        to_ip_address(SERVER_JPG_HOST), SERVER_JPG_PORT,
        urlparse(str(request.url)).path)
    async_client = httpx_client_wrapper()
    file = {'image': (image.filename, image.file, image.content_type)}
    res = await async_client.post(outbound_url, files=file)

    if res.status_code != 201:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    return res.text

@convert_router.post('/to-png', response_model=str, status_code=201)
@rate_limiter(API_MAX_REQUESTS_PER_DAY)
async def convert_to_png(image: UploadFile, request: Request) -> Any:
    outbound_url = "http://{}:{}{}".format(
        to_ip_address(SERVER_PNG_HOST), SERVER_PNG_PORT,
        urlparse(str(request.url)).path)
    async_client = httpx_client_wrapper()
    file = {'image': (image.filename, image.file, image.content_type)}
    res = await async_client.post(outbound_url, files=file)

    if res.status_code != 201:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    return res.text

@convert_router.post('/to-webp', response_model=str, status_code=201)
@rate_limiter(API_MAX_REQUESTS_PER_DAY)
async def convert_to_webp(image: UploadFile, request: Request) -> Any:
    outbound_url = "http://{}:{}{}".format(
        to_ip_address(SERVER_WEBP_HOST), SERVER_WEBP_PORT,
        urlparse(str(request.url)).path)
    async_client = httpx_client_wrapper()
    file = {'image': (image.filename, image.file, image.content_type)}
    res = await async_client.post(outbound_url, files=file)

    if res.status_code != 201:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    return res.text