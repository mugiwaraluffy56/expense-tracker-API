from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Float
from datetime import date
from typing import Optional

Base = declarative_base()

class Expense(Base):
    __tablename__ = "expenses"

    id: Integer
    title: String
    amount: Float
    date: date
    category: Optional[str] = None