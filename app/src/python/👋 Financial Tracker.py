""" A simple streamlit app for financial tracking.
TODOs:
- Create a streamlit page for data input.
- Create a db for data storage.
- Create visualizations.
- Create Signup
- Cipher db.
"""

import streamlit as st
from orm import *

st.set_page_config(page_title="Financial Tracker", page_icon="👋")
st.sidebar.header("👋 Financial Tracker")

st.write("# Financial Tracker")
