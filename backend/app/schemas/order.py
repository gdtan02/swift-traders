from pydantic import BaseModel
from typing import Union, List, Dict, Any, Optional
from datetime import date, datetime
from enum import Enum
from uuid import UUID, uuid4

from backend.app.schemas.trade import Asset

class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop-limit"
    TAKE_PROFIT = "take-profit"

class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"
    
class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REJECTED = "rejected"
    CANCELLED = "cancelled"

class Order(BaseModel):
    id: Optional[UUID] = uuid4()
    timestamp: Union[date, datetime]
    asset: Asset 
    orderType: OrderType
    side: OrderSide
    quantity: float
    price: Optional[float] = None
    status: OrderStatus = OrderStatus.PENDING
    executionPrice: Optional[float] = None
    executionTimestamp: Optional[datetime] = None
    cancelReason: Optional[str] = None
    pnl: Optional[float] = None
    
    @property
    def value(self) -> float:
        if self.executionPrice is not None:
            return self.quantity * self.executionPrice
        elif self.price is not None:
            return self.quantity * self.price
        else:
            return 0.0
     