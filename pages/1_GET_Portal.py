import streamlit as st
from utils.google_sheet import add_assignment

st.title("GET Portal")

GETS = [
    "Uzair Saiyed",
    "Kaif Qureshi",
    "Alisha Arora",
    "Karan Khetani",
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
    "Parth Shah",
    "Dhaval Mehta"
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

    try:

        add_assignment(
            [
                employee_name,
                "GET",
                "",
                project_code,
                task_name,
                senior_name,
                approx_duration,
                str(start_date),
                str(end_date),
                "Pending"
            ]
        )

        st.success("Assignment Submitted")

    except Exception as e:

        st.error(str(e))
