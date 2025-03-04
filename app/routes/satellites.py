from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import Satellite
from app.services.satellite_service import get_all_satellites, get_satellite_by_id

router = APIRouter(prefix="/satellites", tags=["Satellites"])

@router.get("/", response_model=List[Satellite])
def get_satellites():
    return get_all_satellites()

@router.get("/{satellite_id}", response_model=Satellite)
def get_satellite(satellite_id: str):
    satellite = get_satellite_by_id(satellite_id)
    if not satellite:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return satellite
