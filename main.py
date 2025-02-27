from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import LoanRequest
from services import generate_schedule

app = FastAPI()

# ✅ CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://loan-repayment-frontend.vercel.app"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.get("/")
def home():
    return {"message": "Loan Repayment API is working!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/schedule")
def get_schedule(data: LoanRequest):
    return generate_schedule(data)  

@app.options("/{full_path:path}")
async def preflight_handler():
    return {"message": "CORS preflight request successful"}
