from fastapi import FastAPI
from models import LoanRequest
from services import generate_schedule
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
origins = [
    "http://localhost:3000",  # Allow frontend requests
    "https://your-frontend.com"  # Add your production frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allow all headers
)

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
