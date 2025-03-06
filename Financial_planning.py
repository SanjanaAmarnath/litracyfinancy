import streamlit as st
import pandas as pd

def show():
    st.title("Financial Planning")
    st.write("Plan your financial future by setting savings goals and tracking your progress.")

    # Input fields for financial goals
    st.subheader("Set Your Financial Goals")
    goal_name = st.text_input("Goal Name (e.g., Buy a House, Education Fund, Travel)")
    goal_amount = st.number_input("Target Amount (₹)", min_value=0.0, format="%.2f")
    monthly_savings = st.number_input("Monthly Savings (₹)", min_value=0.0, format="%.2f")
    years = st.number_input("Years to Achieve Goal", min_value=1, max_value=50, step=1)

    # Calculate total savings over time
    total_savings = monthly_savings * 12 * years

    # Display Results
    if st.button("Calculate Savings Progress"):
        st.subheader("Savings Projection")
        st.write(f"**Target Goal:** ₹{goal_amount:,.2f}")
        st.write(f"**Estimated Savings in {years} years:** ₹{total_savings:,.2f}")

        if total_savings >= goal_amount:
            st.success("🎉 Congratulations! You are on track to achieve your goal.")
        else:
            shortfall = goal_amount - total_savings
            st.warning(f"⚠️ You need to save an additional ₹{shortfall:,.2f} to reach your goal.")

    # Financial Tips
    st.subheader("Financial Planning Tips 💡")
    st.write("""
    - **Start Early:** The sooner you start saving, the more you'll accumulate.
    - **Track Expenses:** Keep a record of your spending to find saving opportunities.
    - **Invest Wisely:** Consider mutual funds, SIPs, or other investments to grow your savings.
    - **Reduce Unnecessary Expenses:** Identify areas where you can cut back.
    - **Emergency Fund:** Always keep at least 6 months' worth of expenses as a backup.
    """)
#import streamlit as st


# Initialize financial data in session state
if "financial_data" not in st.session_state:
    st.session_state.financial_data = []

def add_transaction(transaction_type, amount, category):
    """Function to add a financial transaction"""
    st.session_state.financial_data.append({
        "Transaction Type": transaction_type,
        "Amount (₹)": amount,
        "Category": category
    })

def show():
    st.title("📊 Financial Tracking")
    st.write("Monitor your financial transactions and stay on top of your money.")

    # User Inputs
    transaction_type = st.selectbox("Transaction Type", ["Income", "Expense"])
    category = st.selectbox("Category", ["Salary", "Food", "Rent", "Savings", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")

    if st.button("Add Transaction"):
        if amount > 0:
            add_transaction(transaction_type, amount, category)
            st.success("Transaction added successfully!")
        else:
            st.error("Please enter a valid amount.")

    # Display Financial Data
    if st.session_state.financial_data:
        df = pd.DataFrame(st.session_state.financial_data)
        st.write("### Financial Transactions")
        st.dataframe(df)

# Run the function when the page loads
show()

