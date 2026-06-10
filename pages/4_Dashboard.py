import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
ALL_EMPLOYEES = [
    "Uzair Saiyed",
    "Kaif Qureshi",
    "Jaimin Prajapati",
    "Nayaabshaad Ansari",
    "Nandini Jadav",
    "Parvej Meman",
    "Chaitrang Prabhu"
]
st.title("Management Dashboard")

conn = sqlite3.connect("tracker.db")

df = pd.read_sql_query(
    "SELECT * FROM assignments",
    conn
)

conn.close()

approved_employees = []

if not df.empty:

    approved_employees = df[
        df["status"] == "Approved"
    ]["employee_name"].unique().tolist()

busy = len(approved_employees)

available = len(ALL_EMPLOYEES) - busy

pending = len(
    df[df["status"] == "Pending"]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Busy",
    busy
)

col2.metric(
    "Available",
    available
)

col3.metric(
    "Pending",
    pending
)

st.divider()

st.subheader("All Requests")

st.subheader("Resource Overview")

st.dataframe(
    df[
        [
            "employee_name",
            "employee_type",
            "project_code",
            "project_description",
            "senior_name",
            "approx_duration",
            "start_date",
            "end_date",
            "status"
        ]
    ],
    use_container_width=True
)
st.divider()

st.subheader("Weekly Availability Matrix")
days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri"
]
availability_data = []

for employee in ALL_EMPLOYEES:

    row = {
        "Employee": employee
    }

    for day in days:
        row[day] = "🟢"

    availability_data.append(row)

# LOOP ENDS HERE

availability_df = pd.DataFrame(
    availability_data
)

st.dataframe(
    availability_df,
    use_container_width=True
)
