# src/api/prices.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.models.db import get_db
from src.models.schemas import PriceRow
import src.crud as crud
from src.schemas import PriceCreate, PriceUpdate, PriceOut

router = APIRouter()

@router.get("/daily", response_model=list[PriceRow])
def get_daily_prices(
    ticker: str = Query(..., description="Company ticker"),
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    data = crud.get_daily_prices(db, ticker, start_date, end_date, limit)
    if not data:
        raise HTTPException(status_code=404, detail="No prices found")
    return [dict(row) for row in data]
