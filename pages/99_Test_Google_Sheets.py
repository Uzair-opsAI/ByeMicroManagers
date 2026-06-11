import streamlit as st
from utils.google_sheet import sheet

st.write("Worksheet Name:")
st.write(sheet.title)

st.write(sheet.get_all_values())
