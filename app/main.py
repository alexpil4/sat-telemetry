from fastapi import FastAPI
from app.routes import satellites, telemetry, alerts

app = FastAPI(
    title="Satellite Monitoring API 🛰️",
    description="An API for monitoring satellite telemetry and alerts (mocks) in real-time.",
    version="1.0.0"
)

# Include the router within the app
app.include_router(satellites.router)
app.include_router(telemetry.router)
app.include_router(alerts.router)
