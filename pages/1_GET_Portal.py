import streamlit as st
import sqlite3
from utils.db import init_db

init_db()
st.title("GET Portal")

GETS = [
    "Uzair Saiyed",
    "Kaif Qureshi",
    "Jaimin Prajapati"
]

SENIORS = [
    "VineetKumar Sandil",
    "Nilay Patel",
    "Viral Shah",
    "Sameer Jain",
    "Chandresh Salakiya",
    "Ramesh Prajapati",
    "Hardik Gohil",
    "Kamlesh Prajapati",
    "Rintu Midday",
    "Nakul Bhatt",
    "Kaustubh Soman",
    "Parth Shah"
]

employee_name = st.selectbox(
    "GET Name",
    GETS
)

project_code = st.text_input(
    "Project Code"
)

task_name = st.text_area(
    "Task Assigned"
)

senior_name = st.selectbox(
    "Assigned By",
    SENIORS
)

approx_duration = st.number_input(
    "Approx Duration (Hours)",
    min_value=1,
    max_value=500,
    value=8
)

start_date = st.date_input(
    "Start Date"
)

end_date = st.date_input(
    "End Date"
)

if st.button("Submit Task"):

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(assignments)")
    columns = cursor.fetchall()
    
    st.write("Current Database Columns:")
    st.write(columns)
    cursor.execute("""
    INSERT INTO assignments
    (
        employee_name,
        employee_type,
        project_code,
        project_description,
        senior_name,
        approx_duration,
        start_date,
        end_date,
        status
    )
    VALUES (?,?,?,?,?,?,?,?,?)
    """,
    (
        employee_name,
        "GET",
        project_code,
        task_name,
        senior_name,
        approx_duration,
        str(start_date),
        str(end_date),
        "Pending"
    ))

    conn.commit()
    conn.close()

    st.success("Assignment Submitted")
