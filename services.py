from datetime import datetime, timedelta
import math
from models import LoanRequest

def calculate_emi(principal, rate, tenure):
    monthly_rate = (rate / 100) / 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
    return round(emi, 2)

def generate_schedule(data: LoanRequest):
    schedule = []
    principal = data.principal
    tenure = data.tenure
    interest_rate = data.interest_rate
    moratorium = data.moratorium_period
    emi_frequency = data.emi_frequency
    disbursement_date = datetime.strptime(data.disbursement_date, "%Y-%m-%d")

    interval = 1 if emi_frequency == "monthly" else 3 if emi_frequency == "quarterly" else None
    if interval is None:
        return {"error": "Invalid EMI frequency"}

    emi = calculate_emi(principal, interest_rate, tenure)
    current_date = disbursement_date + timedelta(days=moratorium * 30)  # Start after moratorium

    for i in range(1, tenure + 1):
        interest = round(principal * (interest_rate / 100) / 12, 2)
        principal_component = round(emi - interest, 2)
        principal -= principal_component
        schedule.append({
            "installment_no": i,
            "date": current_date.strftime("%Y-%m-%d"),
            "emi": emi,
            "principal_component": principal_component,
            "interest_component": interest,
            "remaining_principal": round(principal, 2)
        })
        current_date += timedelta(days=interval * 30)

    return schedule
