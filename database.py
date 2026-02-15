from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
DBurl = "postgresql://postgres:mohana123@localhost:5432/expenses"
engine = create_engine(DBurl)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)