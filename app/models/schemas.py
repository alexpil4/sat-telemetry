from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
import uuid


# Pydantic schema model

class SignalHistory(BaseModel):
    signal_power: float
    signal_noise_ratio: float
    frequency_mhz: float
    timestamp: datetime
class Signal(BaseModel): 
    signal_power: float
    signal_noise_ratio: float
    frequency_mhz: float
    last_signal_update: datetime
    signal_history: List[SignalHistory]

class Position(BaseModel):
    height: float
    latitude: float
    longitude: float
    last_updated: datetime
    
class PowerStatus(BaseModel):
    power_status: str
    last_power_status_at: datetime
    
class LastEvent(BaseModel):
    last_event: str
    last_event_at: datetime

class Telemetry(BaseModel):
    id: str
    velocity_kms: float
    temperature_c: float
    power_status: PowerStatus
    last_event: LastEvent
    position: Position
    signal: Signal
    
class Satellite(BaseModel):
    id: str
    norad_id: int
    orbit: str
    name: str
    status: str
    telemetry: Telemetry
    
class Alert(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    satellite_id: str
    issue: str
    severity: str
    
class AlertResponse(BaseModel):
    message: str
    data: Alert
