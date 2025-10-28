import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from pathlib import Path

# 🔹 Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# 🔹 Define DB connection
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print("Connecting to DB:", DATABASE_URL)

# 🔹 Path to merged CSV
DATA_FILE = Path(r"C:\Users\auguc\OneDrive\Documents\GitHub\mse-api-assignment-main\mse-api-assignment-main\data\csv_files\merged.csv")

if not DATA_FILE.exists():
    print(f"⚠️ File not found: {DATA_FILE}")
    exit()

# 🔹 Load CSV
df = pd.read_csv(DATA_FILE)
print("🧾 Columns found in CSV:")
print(df.columns.tolist())
print("First few rows:")
print(df.head())

# 🔹 Connect to DB
engine = create_engine(DATABASE_URL)

# 🔹 Ensure column names match your table
df.columns = df.columns.str.lower()
expected_cols = ['company_name', 'ticker', 'isin', 'listing_price', 'date_listed']
df = df[expected_cols]

# 🔹 Insert data
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['open'] = pd.to_numeric(df['open'], errors='coerce')
df = df.dropna(subset=['ticker', 'date'])
df = df.drop_duplicates(subset=['ticker', 'date'])

try:
    df.to_sql('daily_prices', engine, if_exists='append', index=False)
    print(f"\n✅ {len(df)} rows inserted successfully into daily_prices.")
except Exception as e:
    print("❌ Error inserting data:", e)
