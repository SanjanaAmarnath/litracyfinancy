import streamlit as st
import numpy as np

def calculate_sip(amount, rate, years):
    n = years * 12
    r = (rate / 100) / 12
    future_value = amount * (((1 + r) ** n - 1) / r) * (1 + r)
    return future_value

def show():
    st.title("SIP Calculator")
    
    amount = st.number_input("Monthly Investment (₹)", min_value=100.0, step=100.0)
    rate = st.number_input("Expected Annual Return (%)", min_value=1.0, max_value=30.0, step=0.1)
    years = st.number_input("Investment Duration (years)", min_value=1, max_value=50, step=1)

    if st.button("Calculate SIP Returns"):
        maturity = calculate_sip(amount, rate, years)
        st.success(f"Your Investment Value after {years} years: ₹{maturity:.2f}")
show() 