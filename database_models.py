from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Date, Column

class Base(DeclarativeBase):
    pass

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(Date)
    category = Column(String(50), nullable=True)