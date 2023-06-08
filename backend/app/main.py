import uvicorn
from fastapi import FastAPI

from src.database.connections import Database
from src.routers.users import  convert_router

app = FastAPI()

app.include_router(convert_router, prefix="/convert", tags=["Convert"])

@app.on_event("startup")
async def on_startup():
    Database()

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8004, reload=True)