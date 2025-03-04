import random
import uuid
import threading
import time

from app.models.schemas import Alert, AlertResponse, Satellite, Telemetry
from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
from typing import List




# FastAPI instance
app = FastAPI(
    title="Satellite Monitoring API 🛰️",
    description="An API for monitoring satellite telemetry and alerts (mocks) in real-time.",
    version="1.0.0"
)

# Mock database
satellites = {}
alerts = {}


# Generate mock satellites
def create_satellite(name: str, status: str):
    satellite_id = str(uuid.uuid4())
    satellites[satellite_id] = {
        "id": satellite_id,
        "name": name,
        "status": status,
        "telemetry": {
            "id": satellite_id,
            "velocity_kms": round(random.uniform(7.5, 8.0), 2),
            "temperature_c": round(random.uniform(-100, 50), 1),
            "power_status": {
                "power_status": random.choice(["Nominal", "Low Power", "Critical" ]),
                "last_power_status_at": datetime.now(timezone.utc)
            },
            "last_event": {
                "last_event": random.choice(["Solar Flare Detected", "Thruster Adjustment", "System Check Complete", "Calibration"]),
                "last_event_at": datetime.now(timezone.utc)
            }
        }
    }

# Satellites
create_satellite("Hubble Space Telescope", "Operational")
create_satellite("Sentinel-5P", "Operational")
create_satellite("ISS", "Operational")
create_satellite("Sentinel-2A", "Operational")

# Telemetry mock data generator
def generate_telemetry(satellite_id: str):
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
    
# Alert mock data generator
def generate_alert(data: AlertResponse):
    alert_id = str(uuid.uuid4())
    alerts[alert_id] = {
        "id": alert_id,
        "satellite_id": data.satellite_id,
        "issue": data.issue,
        "severity": data.severity,
        "created_at": datetime.now(timezone.utc)
    }

# Function to update power_status every 30 minutes
def update_power_status():
    while True:
        # 30 minutes
        time.sleep(1800)
        for sat_id in satellites:
            satellites[sat_id]["telemetry"]["power_status"]["power_status"] = random.choice(["Nominal", "Low Power", "Critical"])
            satellites[sat_id]["telemetry"]["power_status"]["last_power_status_at"] = datetime.now(timezone.utc)


# Start background thread
threading.Thread(target=update_power_status, daemon=True).start()

# Endpoints
@app.get("/satellites", response_model=List[Satellite])
def get_satellites():
    return list(satellites.values())

@app.get("/satellites/{satellite_id}", response_model=Satellite)
def get_satellite(satellite_id: str):
    if satellite_id not in satellites:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return satellites[satellite_id]

@app.get("/satellites/{satellite_id}/telemetry", response_model=Telemetry)
def get_telemetry(satellite_id: str):
    if satellite_id not in satellites:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return generate_telemetry(satellite_id)

@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    return list(alerts.values())

@app.post("/alerts", response_model=AlertResponse)
def create_alert(alert: Alert):
    if alert.satellite_id not in satellites:
        raise HTTPException(status_code=404, detail="Satellite not found")
    generate_alert(alert)
    return AlertResponse(message="Alert received", data=alert)
