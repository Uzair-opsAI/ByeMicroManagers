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

busy = len(
    df[df["status"] == "Approved"]
)

available = len(
    df[df["status"] == "Rejected"]
)

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
            "project_code",
            "project_type",
            "priority",
            "senior_name",
            "start_date",
            "end_date",
            "status"
        ]
    ]
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
