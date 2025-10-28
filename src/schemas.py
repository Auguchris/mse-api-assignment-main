# src/api/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class DailyPriceSchema(BaseModel):
    ticker: str
    date: date
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[int]
    trades: Optional[int]

    class Config:
        orm_mode = True
