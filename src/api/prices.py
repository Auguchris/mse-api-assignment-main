# src/api/prices.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models.db import get_db
from models.schemas import PriceRow
import crud

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


@router.get("/range")
def get_price_range(
    ticker: str = Query(...),
    year: int = Query(...),
    month: int | None = None,
    db: Session = Depends(get_db)
):
    data = crud.get_price_range(db, ticker, year, month)
    if not data:
        raise HTTPException(status_code=404, detail="No data for given range")
    return dict(data)


@router.get("/latest")
def get_latest_prices(
    ticker: str | None = None,
    db: Session = Depends(get_db)
):
    data = crud.get_latest_prices(db, ticker)
    if not data:
        raise HTTPException(status_code=404, detail="No latest prices found")
    if isinstance(data, list):
        return [dict(row) for row in data]
    return dict(data)
