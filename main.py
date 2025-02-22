from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Loan Repayment API is working!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Other API endpoints go here
