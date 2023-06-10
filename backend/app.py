import uvicorn
import logging
from fastapi import FastAPI

from src.database.connections import conn
from src.routers.convert import convert_router
from src.routers.health import health_router

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(health_router, prefix="/health", tags=["Health"])

@app.on_event("startup")
async def on_startup():
    conn()

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8004, reload=True, debug=True)