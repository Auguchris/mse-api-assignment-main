from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DailyPrice(Base):
    __tablename__ = "daily_price"

    id = Column(Integer, primary_key=True, index=True)
    counter_id = Column(Integer)
    counter = Column(String)
    trade_date = Column(Date)
    buy_price = Column(Float)
    sell_price = Column(Float)
    today_closing_price = Column(Float)
    previous_closing_price = Column(Float)
    volume_traded = Column(Float)
    # Add the rest of the columns you have in your CSV
