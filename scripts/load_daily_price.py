# src/scripts/load_daily_price.py

import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import numpy as np

# --- Load .env ---
load_dotenv()  # .env iri kuri root ya project
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not set in .env")

# --- CSV path ---
csv_path = Path(r"C:\Users\auguc\OneDrive\Documents\GitHub\mse-api-assignment-main\mse-api-assignment-main\data\master_files\master.csv")
if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found at {csv_path}")

# --- Load CSV ---
df = pd.read_csv(csv_path)

# --- Columns casting ---
int_columns = ['counter_id', 'num_shares_issue', 'volume_traded', 'sen_counter']
float_columns = [
    'daily_range_high', 'daily_range_low', 'buy_price', 'sell_price', 
    'previous_closing_price', 'today_closing_price', 'dividend_mk', 
    'dividend_yield_pct', 'earnings_yield_pct', 'pe_ratio', 'pbv_ratio', 
    'market_capitalization_mkmn', 'profit_after_tax_mkmn', 
    'p1','p2','p3','p4','p5','p6','p7','p8','p9','p10',
    'p11','p12','p13','p14','p15','p16','p17','p18'
]

# --- Safe casting function ---
def safe_int(x):
    try:
        if pd.isna(x) or x == '':
            return 0
        return int(float(x))
    except:
        return 0

def safe_float(x):
    try:
        if pd.isna(x) or x == '':
            return 0.0
        return float(x)
    except:
        return 0.0

# Apply casting
for col in int_columns:
    if col in df.columns:
        df[col] = df[col].apply(safe_int)

for col in float_columns:
    if col in df.columns:
        df[col] = df[col].apply(safe_float)

# --- Connect to DB ---
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db = Session()

# --- Load data into DB ---
try:
    df.to_sql('daily_price', engine, if_exists='append', index=False, method='multi')
    print("Data successfully loaded into daily_price table.")
except Exception as e:
    print("Error loading data into DB:", e)
finally:
    db.close()
