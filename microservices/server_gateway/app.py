import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.convert import convert_router
from src.routers.health import health_router
from src.utils.httpx import httpx_client_wrapper
from config import GATEWAY_PORT, URL_FRONTEND

logging.basicConfig(level=logging.DEBUG)

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

@app.on_event("shutdown")
async def shutdown_event():
    await httpx_client_wrapper.stop()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(health_router, prefix="/health", tags=["Health"])

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=GATEWAY_PORT, reload=False)