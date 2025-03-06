import math

# Format currency to Indian Rupees (₹)
def format_currency(amount):
    return f"₹{amount:,.2f}"

# SIP Calculator: Calculates future value of a Systematic Investment Plan
def calculate_sip(monthly_investment, annual_rate, years):
    n = years * 12  # Convert years to months
    r = (annual_rate / 100) / 12  # Monthly interest rate
    future_value = monthly_investment * (((1 + r) ** n - 1) / r) * (1 + r)
    return future_value

# EMI Calculator: Calculates Equated Monthly Installment
def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = (annual_rate / 100) / 12
    tenure_months = tenure_years * 12
    if monthly_rate == 0:
        return principal / tenure_months  # If rate is 0, divide principal equally
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / (math.pow(1 + monthly_rate, tenure_months) - 1)
    return emi

# Calculate profit/loss percentage
def calculate_profit_loss(investment, current_value):
    return ((current_value - investment) / investment) * 100 if investment > 0 else 0

# Function to validate user input for positive numbers
def validate_positive_input(value):
    return value if value >= 0 else 0
