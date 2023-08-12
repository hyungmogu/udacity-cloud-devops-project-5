import uvicorn
import logging
import redis
import redis.asyncio as redis_async
from urllib.parse import quote
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi_limiter import FastAPILimiter

from src.routers.convert import convert_router
from src.routers.health import health_router
from src.utils.httpx import httpx_client_wrapper
from config import REDIS_HOST, REDIS_PASSWORD, GATEWAY_PORT

logging.basicConfig(level=logging.DEBUG)

async def startup_redis():
    logging.info("Starting up Redis...")
    REDIS_PASSWORD_ECODE_SAFE = quote(REDIS_PASSWORD, safe="")
    try:
        redis_c = redis_async.from_url("redis://{}@{}:6379".format(REDIS_PASSWORD_ECODE_SAFE, REDIS_HOST), encoding="utf-8", decode_responses=True)
        async with redis_c.pipeline(transaction=True) as pipe:
            ok1, ok2 = await (pipe.set("key1", "value1").set("key2", "value2").execute())
        assert ok1
        assert ok2
        await FastAPILimiter.init(redis_c)
    except redis.exceptions.ResponseError as error:
        if error.args[0].startswith('MOVED'):
            # Extract the new node information from the error response
            moved_info = error.args[0].split(' ')
            new_host, new_port = moved_info[2].split(':')

            # Update the Redis client connection to the new node
            redis_c = redis_async.from_url("redis://{}@{}:{}".format(REDIS_PASSWORD_ECODE_SAFE, new_host, new_port), encoding="utf-8", decode_responses=True)
            async with redis_c.pipeline(transaction=True) as pipe:
                ok1, ok2 = await (pipe.set("key1", "value1").set("key2", "value2").execute())
            assert ok1
            assert ok2
            await FastAPILimiter.init(redis_c)
        else:
            # Handle other types of Redis errors
            raise

app = FastAPI()

startup_redis()

@app.exception_handler(redis.exceptions.ResponseError)
async def exception_callback(request: Request, error: redis.exceptions.ResponseError):
    logging.info("Redis exception: {}".format(error.args[0]))
    REDIS_PASSWORD_ECODE_SAFE = quote(REDIS_PASSWORD, safe="")
    # Extract the new node information from the error response
    moved_info = error.args[0].split(' ')
    new_host, new_port = moved_info[2].split(':')

    # Update the Redis client connection to the new node
    redis_c = redis_async.from_url("redis://{}@{}:{}".format(REDIS_PASSWORD_ECODE_SAFE, new_host, new_port), encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_c)
    logging.info("Redis connection updated to new node: {}:{}".format(new_host, new_port))
    logging.info(dir(request))


@app.on_event("startup")
async def startup_event():
    httpx_client_wrapper.start()

@app.on_event("shutdown")
async def shutdown_event():
    await httpx_client_wrapper.stop()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(health_router, prefix="/health", tags=["Health"])

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=GATEWAY_PORT, reload=True) 