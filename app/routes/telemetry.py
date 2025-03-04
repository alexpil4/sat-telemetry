from fastapi import APIRouter, HTTPException
from app.models.schemas import Telemetry
from app.services.telemetry_service import get_telemetry_data

router = APIRouter(prefix="/telemetry", tags=["Telemetry"])

@router.get("/{satellite_id}", response_model=Telemetry)
def get_telemetry(satellite_id: str):
    telemetry = get_telemetry_data(satellite_id)
    if not telemetry:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return telemetry
