from sqlalchemy import Column, Integer, String, Float
from .crud import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    symbol = Column(String, unique=True, nullable=False)

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
    open_price = Column(Float, nullable=True)
    close_price = Column(Float, nullable=True)
    volume = Column(Float, nullable=True)
