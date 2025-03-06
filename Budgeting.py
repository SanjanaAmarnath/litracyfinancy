"""
import streamlit as st

def show():
    st.title("Budgeting Tool")
    income = st.number_input("Enter your monthly income:", min_value=0.0, format="%.2f")
    essentials = st.number_input("Essentials (Rent, Bills, Food):", min_value=0.0, format="%.2f")
    savings = st.number_input("Savings & Investments:", min_value=0.0, format="%.2f")
    discretionary = st.number_input("Discretionary Spending:", min_value=0.0, format="%.2f")

    total_expense = essentials + savings + discretionary
    remaining = income - total_expense

    st.subheader("Summary")
    st.write(f"Total Expenses: ₹{total_expense:.2f}")
    st.write(f"Remaining Balance: ₹{remaining:.2f}")

    if remaining < 0:
        st.error("Your expenses exceed your income! Consider adjusting your budget.")
"""
import streamlit as st

def show():
    st.title("Budgeting")
    st.write("Welcome to the Budgeting section! Here, you can plan and track your budget effectively.")
    
    # Sample Budgeting Form
    income = st.number_input("Enter your monthly income:", min_value=0.0, format="%.2f")
    expenses = st.number_input("Enter your total monthly expenses:", min_value=0.0, format="%.2f")
    
    if income > 0:
        savings = income - expenses
        st.write(f"💰 Your estimated savings: **₹{savings:,.2f}**")
        if savings < 0:
            st.warning("⚠️ You are overspending! Consider reducing your expenses.")
        elif savings == 0:
            st.info("🔄 You're breaking even—try to save a portion of your income.")
        else:
            st.success("🎉 Great job! You're saving money.")

if __name__ == "__main__":
    show()
