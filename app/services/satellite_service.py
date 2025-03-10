import random
import uuid
import threading
from datetime import datetime, timezone


# DB mock
satellites = {}

def calculateOrbit(height: float):
    if 160 <= height <= 2000:
        return 'LEO'
    elif 2000 < height < 35786:
        return 'MEO'
    elif height >= 35786:
        return 'GEO'
    else:
        return 'OTHER'
        

def create_satellite(name: str, status: str):
    satellite_id = str(uuid.uuid4())
    height = round(random.uniform(160, 35786), 2)
    satellites[satellite_id] = {
        "id": satellite_id,
        "name": name,
        "norad_id": random.randint(10000, 40000),
        "orbit": calculateOrbit(height),
        "status": status,
        "telemetry": {
            "id": satellite_id,
            "velocity_kms": round(random.uniform(7.5, 8.0), 2),
            "temperature_c": round(random.uniform(-80, 80), 2),
            "power_status": {
                "power_status": random.choice(["Nominal", "Low Power", "Critical"]),
                "last_power_status_at": datetime.now(timezone.utc)
            },
            "last_event": {
                "last_event": random.choice(["Solar Flare Detected", "Thruster Adjustment", "System Check Complete"]),
                "last_event_at": datetime.now(timezone.utc)
            },
            "position": {
                "height": height,
                "latitude": round(random.uniform(-90, 90), 6),
                "longitude": round(random.uniform(-180, 180), 6),
                "last_updated": datetime.now(timezone.utc)
            },
           "signal": {
                "signal_power": round(random.uniform(25.0, 45.0), 2), 
                "signal_noise_ratio": round(random.uniform(10, 30), 2),
                "frequency_mhz": round(random.uniform(1000, 20000), 2),
                "last_signal_update": datetime.now(timezone.utc), 
                "signal_history": []
            }
        }
    }
# Mock the data generation for position and signal
def update_satellite_data():
    for satellite in satellites.values():
        # Position
        satellite["telemetry"]["position"]["latitude"] = round(random.uniform(-90, 90), 6)
        satellite["telemetry"]["position"]["longitude"] = round(random.uniform(-180, 180), 6)
        satellite["telemetry"]["position"]["last_updated"] = datetime.now(timezone.utc)
        
        # Signal
        satellite["telemetry"]["signal"]["signal_power"] = round(random.uniform(25.0, 45.0), 2)
        satellite["telemetry"]["signal"]["signal_noise_ratio"] = round(random.uniform(10, 30), 2)
        satellite["telemetry"]["signal"]["frequency_mhz"] = round(random.uniform(1000, 20000), 2)
        satellite["telemetry"]["signal"]["last_signal_update"] = datetime.now(timezone.utc)

        # Create a signal slot
        new_signal_entry = {
            "signal_power": satellite["telemetry"]["signal"]["signal_power"],
            "signal_noise_ratio": satellite["telemetry"]["signal"]["signal_noise_ratio"],
            "frequency_mhz": satellite["telemetry"]["signal"]["frequency_mhz"],
            "timestamp": datetime.now(timezone.utc)
        }
        
        # Add new slot to history
        signal_history = satellite["telemetry"]["signal"]["signal_history"]
        signal_history.append(new_signal_entry)

        # Save till 10 slot, it remove the oldest
        if len(signal_history) > 10:
            signal_history.pop(0)    
               
    threading.Timer(5.0, update_satellite_data).start() # 5 sec

def get_all_satellites():
    return list(satellites.values())

def get_satellite_by_id(satellite_id: str):
    return satellites.get(satellite_id, None)

# Satellites
create_satellite("METEOR M2", "operational")
create_satellite("Sentinel-5P", "operational")
create_satellite("STARLINK-1130", "not operational")
create_satellite("Sentinel-2A", "operational")

# Update satellite position
update_satellite_data()