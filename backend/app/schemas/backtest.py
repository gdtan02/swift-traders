from datetime import date, datetime
from typing import Any, Dict, List, Union
from pydantic import BaseModel, field_validator

from backend.app.schemas.order import Order
from backend.app.schemas.trade import Asset, TradeMetrics

# Backtest API endpoints
class BacktestRequestModel(BaseModel):
    """Standardized request model for backtest endpoints"""
    strategyName: str
    startDate: Union[date, datetime]
    endDate: Union[date, datetime]
    assets: List[Asset] = [Asset()]
    initial_capital : float = 100000.0

    @field_validator('endDate')
    def end_date_after_start_date(cls, v: Union[date, datetime], values: Dict[str, Any]) -> Union[date, datetime]:
        if "startDate" in values and v < values["startDate"]:
            raise ValueError("endDate must be after startDate")
        return v
    
class BacktestResponseModel(BaseModel):
    strategyName: str
    startDate: datetime
    endDate: datetime
    initialCapital: float
    finalEquity: float
    totalReturn: float
    annualizedReturn: float
    tradeMetrics: TradeMetrics 
    equityCurve: Dict[datetime, float]
    drawdownCurve: Dict[datetime, float]
    trades = List[Order]