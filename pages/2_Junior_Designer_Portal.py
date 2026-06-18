import streamlit as st
from utils.google_sheet import add_assignment

st.title("Junior Designer Portal")

DESIGNERS = [
    "Nikhil Padvi",
    "Nisha Prajapati",
    "Dharmendra Gohil"
]

SENIORS = [
    "Mumbai Office",
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
    "Junior Designer Name",
    DESIGNERS
)

work_allocation_status = st.selectbox(
    "Work Hours Assigned?",
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

if st.button("Submit Assignment"):

    status = "Pending"

    if senior_name == "Mumbai Office":
        status = "Approved"

    add_assignment(
        [
            employee_name,
            "Junior Designer",
            work_allocation_status,
            project_code,
            task_name,
            senior_name,
            approx_duration,
            str(start_date),
            str(end_date),
            status
        ]
    )

    st.success(
        "Assignment Submitted"
    )
