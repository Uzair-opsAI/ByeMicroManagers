import streamlit as st

from utils.google_sheet import (
    get_assignments,
    update_status
)

PASSWORD = "Kent@2026"

entered_password = st.text_input(
    "Senior Access Password",
    type="password"
)

if entered_password != PASSWORD:
    st.warning("Senior Login Required")
    st.stop()

st.title("Senior Approval Portal")

df = get_assignments()

if len(df) == 0:

    st.info(
        "No requests submitted yet."
    )

else:

    pending_df = df[
        df["status"] == "Pending"
    ]

    if len(pending_df) == 0:

        st.success(
            "No pending requests."
        )

    for index, row in pending_df.iterrows():

        st.subheader(
            f"{row['employee_name']} | {row['project_code']}"
        )

        st.write(
            f"Description: {row['project_description']}"
        )

        st.write(
            f"Senior: {row['senior_name']}"
        )
        st.write(
            f"Work Hours Assigned: {row['work_hours_assigned']}"
        )
        st.write(
            f"Duration: {row['approx_duration']} Hours"
        )

        st.write(
            f"Start: {row['start_date']}"
        )

        st.write(
            f"End: {row['end_date']}"
        )

        col1, col2 = st.columns(2)

        google_sheet_row = index + 2

        with col1:

            if st.button(
                f"Approve_{index}"
            ):

                update_status(
                    google_sheet_row,
                    "Approved"
                )

                st.rerun()

        with col2:

            if st.button(
                f"Reject_{index}"
            ):

                update_status(
                    google_sheet_row,
                    "Rejected"
                )

                st.rerun()

        st.divider()
