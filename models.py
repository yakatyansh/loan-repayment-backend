from pydantic import BaseModel

class LoanRequest(BaseModel):
    disbursement_date: str  
    principal: float
    tenure: int  
    emi_frequency: str  
    interest_rate: float  
    moratorium_period: int  
