import streamlit as st
import sqlite3

st.title("Junior Engineer Portal")

JUNIORS = [
    "Nayaabshaad Ansari",
    "Nandini Jadav",
    "Parvej Meman",
    "Chaitrang Prabhu"
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
    "Junior Engineer Name",
    JUNIORS
)

work_allocation_status = st.selectbox(
    "Work hours assigned?",
    [
        "Assigned",
        "Not Assigned"
    ]
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

if st.button("Submit Junior Assignment"):

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO assignments
    (
        employee_name,
        employee_type,
        work_hours_assigned,
        project_code,
        project_description,
        senior_name,
        approx_duration,
        start_date,
        end_date,
        status
    )
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """,
    (
        employee_name,
        "Junior Engineer",
        work_allocation_status,
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
