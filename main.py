from fastapi import FastAPI, Depends
# from models import Expense
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import database_models

app = FastAPI()

database = database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.commit()

@app.get("/")
def read_root():
    return {"Expense": "Tracker"}

@app.get("/status")
def read_status():
    return {"status": "okay"}

@app.get("/expenses")
def get_expenses(db: Session = da):
