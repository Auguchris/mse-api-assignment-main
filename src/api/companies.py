# src/api/companies.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src import models

router = APIRouter()

@router.get("/companies")
def read_companies(db: Session = Depends(get_db)):
    companies = db.query(models.Company).all()
    return companies
# src/api/companies.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src import models

router = APIRouter()

@router.get("/")
def read_companies(db: Session = Depends(get_db)):
    companies = db.query(models.Company).all()
    return companies
