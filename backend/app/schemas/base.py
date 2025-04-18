from typing import Optional, Generic, TypeVar
from pydantic import BaseModel
from enum import Enum

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    """Standardized response model for all API endpoints"""
    success: bool
    message: Optional[str] = None
    data: Optional[T] = None
    
class DataFrequency(str, Enum):
    "HOURLY" = "hour"
    "DAILY" = "day"
