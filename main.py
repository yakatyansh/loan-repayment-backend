from fastapi import FastAPI
from models import LoanRequest
from services import generate_schedule

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Loan Repayment API is working!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/schedule")
def get_schedule(data: LoanRequest):
    schedule = generate_schedule(data)
    return schedule

# Other API endpoints go here
