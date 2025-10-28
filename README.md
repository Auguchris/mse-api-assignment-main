# MSE API Assignment Project

This project is a Python API for data processing and analysis.

## Features
- Data extraction and processing
- PostgreSQL database integration
- ML model predictions

## How to run
1. Create virtual environment: `python -m venv .venv`
2. Activate it: `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run main script: `python src/main.py`
# MSE API (FastAPI Project)
This API provides endpoints for company and price data.

## Features
- GET /companies
- GET /companies/{ticker}
- GET /prices/daily
- GET /prices/rangegi
- GET /prices/latest

## Run locally
```bash
uvicorn src.main:app --reload


## Author
Augustin Ndayambaje

