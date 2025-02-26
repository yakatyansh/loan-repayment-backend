from fastapi import FastAPI, Response
from models import LoanRequest
from services import generate_schedule
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this for your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Loan Repayment API is working!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/schedule")
def get_schedule(data: LoanRequest, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    schedule = generate_schedule(data)
    return schedule

# Other API endpoints go here
