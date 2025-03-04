from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import Alert, AlertResponse
from app.services.alert_service import create_new_alert, get_all_alerts

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/", response_model=List[Alert])
def get_alerts():
    return get_all_alerts()

@router.post("/", response_model=AlertResponse)
def create_alert(alert: Alert):
    alert_created = create_new_alert(alert)
    if not alert_created:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return AlertResponse(message="Alert received", data=alert_created)
