import random
import uuid
from datetime import datetime, timezone
from app.models.schemas import Satellite

# DB mock
satellites = {}

def create_satellite(name: str, status: str):
    satellite_id = str(uuid.uuid4())
    satellites[satellite_id] = {
        "id": satellite_id,
        "name": name,
        "norad_id": random.randint(10000, 40000),
        "status": status,
        "telemetry": {
            "id": satellite_id,
            "velocity_kms": round(random.uniform(7.5, 8.0), 2),
            "temperature_c": round(random.uniform(-100, 50), 1),
            "power_status": {
                "power_status": random.choice(["Nominal", "Low Power", "Critical"]),
                "last_power_status_at": datetime.now(timezone.utc)
            },
            "last_event": {
                "last_event": random.choice(["Solar Flare Detected", "Thruster Adjustment", "System Check Complete"]),
                "last_event_at": datetime.now(timezone.utc)
            }
        }
    }

def get_all_satellites():
    return list(satellites.values())

def get_satellite_by_id(satellite_id: str):
    return satellites.get(satellite_id, None)

# Satellites
create_satellite("METEOR M2", "operational")
create_satellite("Sentinel-5P", "operational")
create_satellite("STARLINK-1130", "not operational")
create_satellite("Sentinel-2A", "operational")
