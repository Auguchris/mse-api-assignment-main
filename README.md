# MSE API Assignment Project
This project implements a PostgreSQL database for Malawi Stock Exchange data and a FastAPI REST API to query companies and daily stock prices
This project also  is a Python API for data processing and analysis.

## Features
- Data extraction and processing
- PostgreSQL database integration
- ML model predictions

## How to run
1. Create virtual environment: `python -m venv .venv`
2. Activate it: `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run main script: `python src/main.py`
# Deliverables on DB

PostgreSQL database (mse_db) with 2 tables: companies and prices_daily

Clean, validated data (no duplicates)

FastAPI endpoints for company and price queries
Database Setup & Schema

Mention database name (mse_db) and tables (companies, prices_daily).

Include column details, which columns allow nulls, primary keys, foreign keys, and unique constraints.

Note handling missing values and duplicates, e.g., UPSERT or unique constraints.

3️⃣ API Endpoints

List all 5 endpoints (/companies, /companies/{ticker}, /prices/daily, /prices/range, /prices/latest) with:

Purpose / description

Path or query parameters

Response format

Examples of usage (like CURL commands)

Mention validation using Pydantic and HTTP status codes (200, 400, 404
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

