import streamlit as st
from utils.db import init_db

init_db()

st.write("Database Recreated")
init_db()

st.set_page_config(
    page_title="ByeMicroManagers",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ByeMicroManagers")

st.subheader(
    "Electrical Engineering Resource Tracker"
)

st.info(
    "Use the menu on the left to access Junior Portal, Senior Portal and Dashboard."
)
