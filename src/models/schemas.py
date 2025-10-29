from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# -----------------------
# Company Schemas
# -----------------------
class CompanyBase(BaseModel):
    name: str = Field(..., example="Example Company")
    symbol: str = Field(..., example="EXC")

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    symbol: Optional[str] = None

class CompanyOut(CompanyBase):
    id: int

    class Config:
        from_attributes = True

# -----------------------
# Price Schemas
# -----------------------
class PriceBase(BaseModel):
    company_id: int
    date: date
    open_price: Optional[float] = None
    close_price: Optional[float] = None
    volume: Optional[float] = None

class PriceCreate(PriceBase):
    pass

class PriceUpdate(BaseModel):
    open_price: Optional[float] = None
    close_price: Optional[float] = None
    volume: Optional[float] = None

class PriceOut(PriceBase):
    id: int

    class Config:
        from_attributes = True
