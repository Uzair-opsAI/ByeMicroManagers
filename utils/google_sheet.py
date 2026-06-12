import streamlit as st
import gspread
import pandas as pd

from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open(
    "Engineering Resource Tracker"
).worksheet(
    "Assignments"
)

def add_assignment(data):

    sheet.append_row(data)
def get_assignments():

    records = sheet.get_all_records()

    return pd.DataFrame(records)

def update_status(row_number, new_status):

    sheet.update_cell(
        row_number,
        10,
        new_status
    )
