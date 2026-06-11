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

# =========================
# DATABASE
# =========================

conn = sqlite3.connect("tracker.db")

df = pd.read_sql_query(
    "SELECT * FROM assignments",
    conn
)

conn.close()

# =========================
# DASHBOARD CARDS
# =========================

today = datetime.today().date()

busy_employees = []

if not df.empty:

    approved_tasks = df[df["status"] == "Approved"]

    for _, task in approved_tasks.iterrows():

        try:

            end_date = datetime.strptime(
                str(task["end_date"]),
                "%Y-%m-%d"
            )

            if end_date >= today:

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

else:

    st.info("No assignments available.")

# =========================
# WEEKLY AVAILABILITY MATRIX
# =========================

st.divider()

st.subheader("Weekly Availability Matrix")

week_dates = []

for i in range(5):

    week_dates.append(
        today + timedelta(days=i)
    )

availability_data = []

for employee in ALL_EMPLOYEES:

    row = {
        "Employee": employee
    }

    # Default = Available
    for date_obj in week_dates:

        column_name = date_obj.strftime("%d-%b")

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

                for date_obj in week_dates:

                    if start_date <= date_obj <= end_date:

                        column_name = date_obj.strftime("%d-%b")

                        row[column_name] = "🔴"

            except:
                pass

    availability_data.append(row)

availability_df = pd.DataFrame(
    availability_data
)

st.dataframe(
    availability_df,
    use_container_width=True
)
