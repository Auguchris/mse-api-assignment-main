from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))  # Encode special chars
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class DailyPrice(Base):
    __tablename__ = "daily_price"

    id = Column(Integer, primary_key=True, index=True)
    counter_id = Column(Integer)
    daily_range_high = Column(Float)
    daily_range_low = Column(Float)
    counter = Column(String)
    buy_price = Column(Float)
    sell_price = Column(Float)
    previous_closing_price = Column(Float)
    today_closing_price = Column(Float)
    volume_traded = Column(Float)
    dividend_mk = Column(Float)
    dividend_yield_pct = Column(Float)
    earnings_yield_pct = Column(Float)
    pe_ratio = Column(Float)
    pbv_ratio = Column(Float)
    market_capitalization_mkmn = Column(Float)
    profit_after_tax_mkmn = Column(Float)
    num_shares_issue = Column(Float)
    trade_date = Column(Date)
    print_time = Column(String)
