from pydantic import BaseModel
from enum import Enum

class SignalAction(str, Enum):
    "BUY" = 1
    "SELL" = -1
    "HOLD" = 0

class Signal(BaseModel):
    timestamp: str
    action: SignalAction