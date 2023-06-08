from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status

from src.database.connections import get_session
from src.services.convert import ConvertServices


convert_router = APIRouter(
    tags=["Convert"]
)