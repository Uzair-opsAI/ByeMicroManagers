import streamlit as st
from utils.google_sheet import sheet

st.title("Google Sheets Debug")

records = sheet.get_all_records()

st.write("Records:")
st.write(records)

st.write("Row 1:")
st.write(sheet.row_values(1))

st.write("All Values:")
st.write(sheet.get_all_values())
