import streamlit as st
from utils.google_sheet import get_assignments
import pandas as pd
from datetime import datetime, timedelta

ALL_EMPLOYEES = [
    "Uzair Saiyed",
    "Kaif Qureshi",
    "Alisha Arora",
    "Karan Khetani",
    "Jaimin Prajapati",
    "Nayaabshaad Ansari",
    "Nandini Jadav",
    "Parvej Meman",
    "Chaitrang Prabhu"
]

st.title("Management Dashboard")

# =========================
# DATABASE
# =========================

# GOOGLE SHEETS

df = get_assignments()
if df.empty:
    st.warning("No assignments found")
    st.stop()
    st.write(df.columns.tolist())
# =========================
# DASHBOARD CARDS
# =========================

today = datetime.today().date()

busy_employees = []

if not df.empty:

    approved_tasks = df[df["status"] == "Approved"]

    for _, task in approved_tasks.iterrows():

        try:
    
            start_date = datetime.strptime(
                str(task["start_date"]),
                "%Y-%m-%d"
            ).date()
    
            end_date = datetime.strptime(
                str(task["end_date"]),
                "%Y-%m-%d"
            ).date()
    
            if start_date <= today <= end_date:
    
                busy_employees.append(
                    task["employee_name"]
                )

        except:
            pass

busy_employees = list(set(busy_employees))

busy = len(busy_employees)

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

# =========================
# RESOURCE OVERVIEW
# =========================

st.divider()

st.subheader("Resource Overview")

if not df.empty:

    resource_df = df[
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
    ]

    resource_df.index = range(
        1,
        len(resource_df) + 1
    )

    st.dataframe(
        resource_df,
        use_container_width=True
    )

else:

    st.info("No assignments available.")

# =========================
# WEEKLY AVAILABILITY MATRIX
# =========================

st.divider()
st.markdown("""
### Legend

🟢 Available

🔴 Work Allocated Without Hours

🔵 Work Allocated With Hours

🟠 Work Allocated (Hours-N/A)
""")
st.subheader("Weekly Availability Matrix")

week_dates = []

current_date = today

while len(week_dates) < 5:

    if current_date.weekday() < 5:
        week_dates.append(current_date)

    current_date += timedelta(days=1)
availability_data = []

for employee in ALL_EMPLOYEES:

    row = {
        "Employee": employee
    }

    # Default = Available
    for date_obj in week_dates:

        column_name = date_obj.strftime("%a %d-%b")
    
        row[column_name] = "🟢"

    # Check Approved Tasks
    if not df.empty:
    
        employee_tasks = df[
            (df["employee_name"] == employee)
            &
            (df["status"] == "Approved")
        ]
    
        for _, task in employee_tasks.iterrows():
    
            try:
    
                start_date = datetime.strptime(
                    str(task["start_date"]),
                    "%Y-%m-%d"
                ).date()
    
                end_date = datetime.strptime(
                    str(task["end_date"]),
                    "%Y-%m-%d"
                ).date()
    
                employee_type = str(
    task.get(
        "employee_type",
        ""
    )
).strip()

work_hours = str(
    task.get(
        "work_hours_assigned",
        ""
    )
).strip()

for date_obj in week_dates:

    if start_date <= date_obj <= end_date:

        column_name = date_obj.strftime(
            "%a %d-%b"
        )

        # GET Logic
        if employee_type == "GET":

            row[column_name] = "🔴"

        # Engineer Logic
        else:

            if work_hours == "Assigned":

                row[column_name] = "🔵"

            elif work_hours == "Not Assigned":

                row[column_name] = "🔴"

            else:

                row[column_name] = "🟠"

except:
    pass

availability_data.append(row)

availability_df = pd.DataFrame(
    availability_data
)

availability_df.index = range(
    1,
    len(availability_df) + 1
)

st.dataframe(
    availability_df,
    use_container_width=True
)
