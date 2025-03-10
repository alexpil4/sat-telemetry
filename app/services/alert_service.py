import uuid
from datetime import datetime, timezone
from app.models.schemas import Alert
from app.services.satellite_service import satellites

# DB mock
alerts = {}

def create_new_alert(alert: Alert):
    if alert.satellite_id not in satellites:
        return None

    alert_id = str(uuid.uuid4())
    alerts[alert_id] = {
        "id": alert_id,
        "satellite_id": alert.satellite_id,
        "issue": alert.issue,
        "severity": alert.severity,
        "created_at": datetime.now(timezone.utc)
    }
    return alerts[alert_id]

def get_all_alerts():
    return list(alerts.values())

def get_alerts_by_satellite_id(satellite_id: str):
    satellite_alerts = [alert for alert in alerts.values() if alert["satellite_id"] == satellite_id]
    return satellite_alerts if satellite_alerts else None
