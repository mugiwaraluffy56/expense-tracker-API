from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import database_models
from datetime import date
from models import Expense

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
def get_expenses(db: Session = Depends(get_db)):
    db_expenses = db.query(database_models.Expense).all()
    if db_expenses:
        return db_expenses
    return "No expenses were Made"

@app.get("/expenses/{id}")
def get_expenses_by_id(id: int,
                        db: Session = Depends(get_db)):
    db_expense = db.query(database_models.Expense).filter(database_models.Expense.id == id).first()
    if db_expense:
        return db_expense
    return "Expense not Found"

@app.get("/expenses/{date}")
def get_expenses_by_date(date: date,
                          db: Session = Depends(get_db)):
    db_expense = db.query(database_models.Expense).filter(database_models.Expense.date == date).first()
    if db_expense:
        return db_expense
    return "Expense not Found"

@app.get("/expenses/{category}")
def get_expense_by_category(category: str,
                             db: Session = Depends(get_db)):
    db_expense = db.query(database_models.Expense).filter(database_models.Expense.category == category).first()
    if db_expense:
        return db_expense
    return "Expense not Found"

@app.post("/expenses")
def add_expense(expense: Expense,
                 db: Session = Depends(get_db)):
    db.add(database_models.Expense(**expense.model_dump()))
    db.commit()
    return {"message": "Expense added successfully"}