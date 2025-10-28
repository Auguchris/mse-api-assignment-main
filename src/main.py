# src/main.py
from fastapi import FastAPI
from api import companies, prices

app = FastAPI(title="MSE API")

app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(prices.router, prefix="/prices", tags=["Prices"])
