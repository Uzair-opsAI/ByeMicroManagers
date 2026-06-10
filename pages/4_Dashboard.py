import streamlit as st
import sqlite3
import pandas as pd

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
