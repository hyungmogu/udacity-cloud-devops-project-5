import redis
from functools import wraps
from urllib.parse import quote
import redis.asyncio as redis_async

from lib.fastapi_limiter.depends import RateLimiter
from lib.fastapi_limiter import FastAPILimiter

from config import API_SECONDS_IN_DAY, REDIS_PASSWORD

def rate_limiter(API_MAX_REQUESTS_PER_DAY: int):
    REDIS_PASSWORD_ECODE_SAFE = quote(REDIS_PASSWORD, safe="")

    def inner(func):
        @wraps(func)
        async def wrapper(request, *args, **kwargs):
            try:
                rate_limiter = RateLimiter(API_MAX_REQUESTS_PER_DAY, API_SECONDS_IN_DAY)
                rate_limiter(request)
            except redis.exceptions.ResponseError as error:
                if error.args[0].startswith('MOVED'):
                    # Extract the new node information from the error response
                    moved_info = error.args[0].split(' ')
                    new_host, new_port = moved_info[2].split(':')

                    # Update the Redis client connection to the new node
                    redis_c = redis_async.from_url("redis://{}@{}:{}".format(REDIS_PASSWORD_ECODE_SAFE, new_host, new_port), encoding="utf-8", decode_responses=True)
                    await FastAPILimiter.init(redis_c)

                    # Retry the rate limiter
                    rate_limiter = RateLimiter(API_MAX_REQUESTS_PER_DAY, API_SECONDS_IN_DAY)
                    rate_limiter(request)
                else:
                    # Handle other types of Redis errors
                    raise

            return await func(request, *args, **kwargs)
        return wrapper
    return inner