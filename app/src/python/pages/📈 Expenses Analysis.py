import streamlit as st
from config import *
from orm import *

st.set_page_config(page_title="Expenses Analysis", page_icon="📈")
st.sidebar.header("📈 Expenses Analysis")

name = st.text_input("Enter the expense short-name", value="")
description = st.text_input("Enter the expense description", value="")
category = st.selectbox("Select category for your expense: ", CATEGORIES)
payment_method = st.selectbox("Select the payment method: ", PAYMENT_METHOD)
currency = st.selectbox("Select the currency: ", CURRENCIES)
amount = st.number_input(
    "Enter the amount: ", min_value=0.0, max_value=100000.0, step=0.25
)
st.button(
    "Add expense",
    on_click=lambda: Expense(
        name=name,
        description=description,
        category=category,
        payment_method=payment_method,
        currency=currency,
        amount=amount,
    ).save(),
)

for expense in Expense.select():
    st.write(expense.name, expense.description, expense.category, expense.amount)
