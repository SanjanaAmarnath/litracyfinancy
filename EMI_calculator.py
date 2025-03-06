import streamlit as st
import math

def calculate_emi(principal, rate, tenure):
    """Calculate the EMI using the formula: EMI = [P * R * (1+R)^N] / [(1+R)^N - 1]"""
    monthly_rate = rate / (12 * 100)  # Convert annual rate to monthly and percentage
    tenure_months = tenure * 12  # Convert years to months

    if monthly_rate == 0:  # Handle zero-interest case
        return principal / tenure_months

    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / (math.pow(1 + monthly_rate, tenure_months) - 1)
    return emi

def show():
    st.title("EMI Calculator")
    st.write("Calculate your Equated Monthly Installment (EMI) easily.")

    # User Inputs
    principal = st.number_input("Loan Amount (₹)", min_value=1.0, value=100000.0, step=1000.0, format="%.2f")
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, value=8.5, step=0.1, format="%.2f")
    tenure = st.number_input("Loan Tenure (Years)", min_value=1, value=5, step=1)

    if st.button("Calculate EMI"):
        emi = calculate_emi(principal, rate, tenure)
        st.success(f"💰 Your EMI is **₹{emi:,.2f}** per month.")

# Remove: if __name__ == "__main__": show()
show()  # Just call the function directly
