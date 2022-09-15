import streamlit as st
from config import *
from orm import *

st.set_page_config(page_title="Savings Analysis", page_icon="📈")
st.sidebar.header("📈 Savings Analysis")

name = st.text_input("Enter the saving short-name", value="")
description = st.text_input("Enter the saving description", value="")
currency = st.selectbox("Select the currency: ", CURRENCIES)
amount = st.number_input(
    "Enter the amount: ", min_value=0.0, max_value=100000.0, step=0.25
)
st.button(
    "Add Saving",
    on_click=lambda: Saving(
        name=name,
        description=description,
        currency=currency,
        amount=amount,
    ).save(),
)

for saving in Saving.select():
    st.write(saving.name, saving.description, saving.amount)
