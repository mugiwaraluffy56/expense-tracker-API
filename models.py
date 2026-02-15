from pydantic import BaseModel
from datetime import date
from typing import Optional


class Expense(BaseModel):
    id : int
    title : str
    amount : float
    date : date
    category : Optional[str] = None