import random
from datetime import datetime, timezone
from app.services.satellite_service import satellites

def get_telemetry_data(satellite_id: str):
    if satellite_id not in satellites:
        return None

    return {
        "id": satellite_id,
        "velocity_kms": round(random.uniform(7.5, 8.0), 2),
        "temperature_c": round(random.uniform(-100, 50), 1),
        "power_status": {
            "power_status": satellites[satellite_id]["telemetry"]["power_status"]["power_status"],
            "last_power_status_at": datetime.now(timezone.utc)
        },
        "last_event": {
            "last_event": random.choice(["Solar Flare Detected", "Thruster Adjustment", "System Check Complete"]),
            "last_event_at": datetime.now(timezone.utc)
        }
    }
