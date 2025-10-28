# src/api/companies.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models.db import get_db
from models.schemas import CompanyOut
import crud

router = APIRouter()

@router.get("/", response_model=list[CompanyOut])
def get_companies(sector: str | None = None, db: Session = Depends(get_db)):
    data = crud.get_companies(db, sector)
    return [dict(row) for row in data]


@router.get("/{ticker}")
def get_company_by_ticker(ticker: str, db: Session = Depends(get_db)):
    data = crud.get_company_by_ticker(db, ticker)
    if not data:
        raise HTTPException(status_code=404, detail="Company not found")
    return dict(data)
