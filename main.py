from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

class LoanRequest(BaseModel):
    disbursement_date: datetime
    principal: float
    tenure: int
    interest_rate: float
    emi_frequency: int
    moratorium_period: int

def calculate_emi(principal, rate, tenure):
    monthly_rate = (rate/100) / 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
    return round(emi, 2)

