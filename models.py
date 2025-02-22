from pydantic import BaseModel

class LoanRequest(BaseModel):
    disbursement_date: str  # Format: "YYYY-MM-DD"
    principal: float
    tenure: int  # In months
    emi_frequency: str  # "monthly", "quarterly"
    interest_rate: float  # Annual interest rate in %
    moratorium_period: int  # In months
