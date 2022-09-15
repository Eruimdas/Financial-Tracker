import streamlit as st
from config import *
from orm import *

st.set_page_config(page_title="Income Analysis", page_icon="📈")
st.sidebar.header("📈 Income Analysis")

name = st.text_input("Enter the income short-name", value="")
description = st.text_input("Enter the income description", value="")
currency = st.selectbox("Select the currency: ", CURRENCIES)
amount = st.number_input(
    "Enter the amount: ", min_value=0.0, max_value=100000.0, step=0.25
)
st.button(
    "Add Income",
    on_click=lambda: Income(
        name=name,
        description=description,
        currency=currency,
        amount=amount,
    ).save(),
)

for income in Income.select():
    st.write(income.name, income.description, income.amount)
