import streamlit as st
import sqlite3
from datetime import date

st.title("Junior Portal")

EMPLOYEES = [
    "Uzair Saiyed",
    "Nayaabshaad Ansari",
    "Parvej Meman",
    "Nandini Jadav",
    "Chaitrang Prabhu",
    "Kaif Qureshi",
    "Jaimin Prajapati",
    "Alisha Arora",
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
    "Parth Shah",
]

employee_name = st.selectbox(
    "Employee Name",
    EMPLOYEES
)

project_code = st.text_input(
    "Project Code"
)

project_description = st.text_area(
    "Project Description"
)

project_type = st.text_input(
    "Project / Task Name"
)

priority = st.selectbox(
    "Priority",
    ["Low","Medium","High","Critical"]
)

senior_name = st.selectbox(
    "Senior Responsible",
    SENIORS
)

start_date = st.date_input(
    "Start Date"
)

end_date = st.date_input(
    "End Date"
)

start_time = st.time_input(
    "Start Time"
)

end_time = st.time_input(
    "End Time"
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
        project_type,
        priority,
        senior_name,
        start_date,
        end_date,
        start_time,
        end_time,
        status
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        employee_name,
        project_code,
        project_description,
        project_type,
        priority,
        senior_name,
        str(start_date),
        str(end_date),
        str(start_time),
        str(end_time),
        "Pending"
    ))

    conn.commit()
    conn.close()

    st.success(
        "Request Submitted Successfully"
    )
