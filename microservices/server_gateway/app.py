import uvicorn
import logging
import redis.asyncio as redis_async
from urllib.parse import quote
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lib.fastapi_limiter import FastAPILimiter

from src.routers.convert import convert_router
from src.routers.health import health_router
from src.utils.httpx import httpx_client_wrapper
from config import REDIS_HOST, REDIS_PASSWORD, GATEWAY_PORT, URL_FRONTEND

logging.basicConfig(level=logging.DEBUG)

async def startup_redis():
    REDIS_PASSWORD_ECODE_SAFE = quote(REDIS_PASSWORD, safe="")
    redis_c = redis_async.from_url("redis://{}@{}".format(REDIS_PASSWORD_ECODE_SAFE, REDIS_HOST), encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_c)

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
    URL_FRONTEND
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    httpx_client_wrapper.start()
    await startup_redis()

@app.on_event("shutdown")
async def shutdown_event():
    await httpx_client_wrapper.stop()
    await FastAPILimiter.close()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(health_router, prefix="/health", tags=["Health"])

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=GATEWAY_PORT, reload=False)