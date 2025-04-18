from typing import Optional
from pydantic import BaseModel

class Asset(BaseModel):
    symbol: str = "btc"
    name: Optional[str] = "BTC-USD"
    
    class Config:
        frozen=True


class TradeMetrics(BaseModel):
    totalTrades: int = 0
    winningTrades: int = 0
    losingTrades: int = 0
    winRate: float = 0.0
    profitFactor: float = 0.0
    maxDrawdown: float = 0.0
    sharpeRatio: float = 0.0
    sortinoRatio: float = 0.0
    calmarRatio: float = 0.0
    volatility: float = 0.0