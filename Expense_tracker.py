import streamlit as st
import pandas as pd

# Initialize session state for expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

def add_expense(description, amount, category):
    """Function to add an expense"""
    st.session_state.expenses.append({
        "Description": description,
        "Amount (₹)": amount,
        "Category": category
    })

def show():
    st.title("💰 Expense Tracker")
    st.write("Track your daily expenses and analyze your spending habits.")

    # Ensure unique keys for each input element
    description = st.text_input("Expense Description", key="expense_desc_1")
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f", key="expense_amt_1")
    category = st.selectbox("Category", ["Food", "Rent", "Shopping", "Bills", "Travel", "Other"], key="expense_cat_1")

    if st.button("Add Expense", key="add_expense_btn"):
        if description and amount > 0:
            add_expense(description, amount, category)
            st.success("Expense added successfully!")
        else:
            st.error("Please enter a valid description and amount.")

    # Display Expenses
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.write("### Expense List")
        st.dataframe(df)

# Run the function when the page loads
show()
