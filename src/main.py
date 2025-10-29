# src/main.py
from fastapi import FastAPI
from src.api import companies, prices  # absolute import from src package

app = FastAPI(title="MSE API")

# Include routers
app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(prices.router, prefix="/prices", tags=["Prices"])

