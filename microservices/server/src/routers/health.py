from fastapi import APIRouter
from src.services.health import HealthServices

health_router = APIRouter(
    tags=["Health"]
)

@health_router.get("/")
async def get_health_check() -> dict:
    services:HealthServices = HealthServices()
    response:dict = services.check_health()
    return response