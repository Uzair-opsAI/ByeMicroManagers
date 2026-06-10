import streamlit as st
import sqlite3

st.title("Junior Portal")

employee_name = st.text_input(
    "Employee Name"
)

project_code = st.text_input(
    "Project Code"
)

project_description = st.text_area(
    "Project Description"
)

priority = st.selectbox(
    "Priority",
    ["Low", "Medium", "High", "Critical"]
)

senior_name = st.selectbox(
    "Senior Responsible",
    [
        "Senior A",
        "Senior B",
        "Senior C"
    ]
)

if st.button("Submit Request"):

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO assignments
    (
        employee_name,
        project_code,
        project_description,
        priority,
        senior_name,
        status
    )
    VALUES (?,?,?,?,?,?)
    """,
    (
        employee_name,
        project_code,
        project_description,
        priority,
        senior_name,
        "Pending"
    ))

    conn.commit()
    conn.close()

    st.success(
        "Request Submitted Successfully"
    )
