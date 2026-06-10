import sqlite3

def init_db():

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT,
        project_code TEXT,
        project_description TEXT,
        priority TEXT,
        senior_name TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
