from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.crud import get_db
from src.models import Price
from src.schemas import PriceCreate, PriceUpdate, PriceOut

router = APIRouter()

@router.post("/", response_model=PriceOut)
def create_price(price: PriceCreate, db: Session = Depends(get_db)):
    db_price = Price(
        company_id=price.company_id,
        date=price.date,
        open_price=price.open_price,
        close_price=price.close_price,
        volume=price.volume
    )
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

@router.get("/", response_model=List[PriceOut])
def read_prices(db: Session = Depends(get_db)):
    return db.query(Price).all()

@router.get("/{price_id}", response_model=PriceOut)
def read_price(price_id: int, db: Session = Depends(get_db)):
    price = db.query(Price).filter(Price.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    return price

@router.put("/{price_id}", response_model=PriceOut)
def update_price(price_id: int, price: PriceUpdate, db: Session = Depends(get_db)):
    db_price = db.query(Price).filter(Price.id == price_id).first()
    if not db_price:
        raise HTTPException(status_code=404, detail="Price not found")
    for field, value in price.dict(exclude_unset=True).items():
        setattr(db_price, field, value)
    db.commit()
    db.refresh(db_price)
    return db_price

@router.delete("/{price_id}")
def delete_price(price_id: int, db: Session = Depends(get_db)):
    db_price = db.query(Price).filter(Price.id == price_id).first()
    if not db_price:
        raise HTTPException(status_code=404, detail="Price not found")
    db.delete(db_price)
    db.commit()
    return {"detail": "Price deleted"}
