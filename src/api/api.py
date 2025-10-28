from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.db_connect import SessionLocal, engine
from src.db import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Daily Price API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Daily Price API is up!"}

@app.get("/prices/")
def get_all_prices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prices = db.query(models.DailyPrice).offset(skip).limit(limit).all()
    return prices

@app.get("/prices/{counter_id}")
def get_price_by_counter(counter_id: int, db: Session = Depends(get_db)):
    price = db.query(models.DailyPrice).filter(models.DailyPrice.counter_id == counter_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Counter not found")
    return price
