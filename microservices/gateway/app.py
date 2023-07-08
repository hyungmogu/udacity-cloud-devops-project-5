import uvicorn
import logging
import redis.asyncio as redis
from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter

from src.routers.convert import convert_router
from src.routers.health import health_router
from src.utils.httpx import httpx_client_wrapper
from config import REDIS_HOST, GATEWAY_PORT

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(health_router, prefix="/health", tags=["Health"])

@app.on_event("startup")
async def startup_event():
    httpx_client_wrapper.start()

    redis_c = redis.from_url("redis://{}".format(REDIS_HOST), encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_c)

@app.on_event("shutdown")
async def shutdown_event():
    await httpx_client_wrapper.stop()


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=GATEWAY_PORT, reload=True) 