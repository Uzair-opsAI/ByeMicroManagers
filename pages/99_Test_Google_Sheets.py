import streamlit as st
from utils.google_sheet import sheet
import streamlit as st

st.write(st.secrets.keys())
st.title("Google Sheets Test")

data = sheet.get_all_records()

st.write(data)
