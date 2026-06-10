import streamlit as st
import sqlite3
import pandas as pd
password = st.text_input(
    "Senior Access Password",
    type="password"
)

if password != "Kent@2026":
    st.warning("Unauthorized Access")
    st.stop()
st.title("Senior Approval Portal")

conn = sqlite3.connect("tracker.db")

df = pd.read_sql_query(
    "SELECT * FROM assignments",
    conn
)

if len(df) == 0:
    st.info("No requests submitted yet.")

else:

    pending_df = df[df["status"] == "Pending"]

    if len(pending_df) == 0:
        st.success("No pending requests.")

    for _, row in pending_df.iterrows():

        st.subheader(
            f"{row['employee_name']} | {row['project_code']}"
        )

        st.write(
            f"Description: {row['project_description']}"
        )

        st.write(
            f"Priority: {row['priority']}"
        )

        st.write(
            f"Senior: {row['senior_name']}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                f"Approve {row['id']}"
            ):

                cursor = conn.cursor()

                cursor.execute(
                    """
                    UPDATE assignments
                    SET status='Approved'
                    WHERE id=?
                    """,
                    (row['id'],)
                )

                conn.commit()

                st.rerun()

        with col2:

            if st.button(
                f"Reject {row['id']}"
            ):

                cursor = conn.cursor()

                cursor.execute(
                    """
                    UPDATE assignments
                    SET status='Rejected'
                    WHERE id=?
                    """,
                    (row['id'],)
                )

                conn.commit()

                st.rerun()

        st.divider()

conn.close()
