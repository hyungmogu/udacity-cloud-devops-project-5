import uvicorn
import logging
from fastapi import FastAPI

from src.routers.convert import convert_router
from src.routers.health import health_router

from config import SERVER_WEBP_PORT

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(health_router, prefix="/health", tags=["Health"])

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=SERVER_WEBP_PORT, reload=False) 