from fastapi import FastAPI
from models import LoanRequest
from services import generate_schedule

app = FastAPI()

@app.post("/generate-schedule/")
async def generate_loan_schedule(loan_data: LoanRequest):
    return {"repayment_schedule": generate_schedule(loan_data)}
