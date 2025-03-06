import streamlit as st
import random

# Set page title and icon
st.title("🌸 Welcome to Financial Empowerment for Women!")
st.write(
    "Take control of your financial future with our easy-to-use tools. "
    "Manage your budget, track expenses, and plan your investments efficiently."
)

# Quick Feature Overview
st.subheader("📌 Explore Our Features")
st.markdown(
    """
    - 💰 **Budgeting** – Plan and track your income & expenses.
    - 📊 **Expense Tracker** – Monitor your spending habits.
    - 📈 **Financial Planning** – Set and achieve your financial goals.
    - 🏦 **SIP Calculator** – Plan systematic investments easily.
    - 💳 **EMI Calculator** – Calculate your loan repayments.
    """
)

# Quick Navigation Buttons
st.subheader("🚀 Get Started")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("💰 Budgeting"):
        st.switch_page("pages/budgeting.py")
with col2:
    if st.button("📊 Expense Tracker"):
        st.switch_page("pages/expense_tracker.py")
with col3:
    if st.button("📈 Financial Planning"):
        st.switch_page("pages/financial_planning.py")

col4, col5 = st.columns(2)
with col4:
    if st.button("🏦 SIP Calculator"):
        st.switch_page("pages/sip_calculator.py")
with col5:
    if st.button("💳 EMI Calculator"):
        st.switch_page("pages/emi_calculator.py")

# Daily Financial Tip Section
st.subheader("💡 Financial Tip of the Day")
financial_tips = [
    "Start saving at least 20% of your income every month.",
    "Invest early to take advantage of compounding returns.",
    "Track your expenses to identify areas where you can cut back.",
    "Avoid unnecessary debt and always pay your credit card bills on time.",
    "Set up an emergency fund covering 6 months of living expenses.",
    "Diversify your investments to minimize risk.",
]
st.info(random.choice(financial_tips))

# Optional: User Profile (If Login is Implemented)
# st.subheader("👩‍💼 Your Profile")
# st.write("Recent activity and personalized insights will be displayed here.")

# Footer
st.markdown("---")
st.write("🔒 **Your financial data is private and secure.**")
st.write("💬 Need help? Visit our [Support Page](#).")
