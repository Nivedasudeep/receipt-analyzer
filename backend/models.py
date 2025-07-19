from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    vendor = Column(String)
    date = Column(String)
    amount = Column(Float)
    currency = Column(String)
    category = Column(String)

class ReceiptIn(BaseModel):
    vendor: str
    date: str
    amount: float
    currency: str
    category: str
