cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    employee_type TEXT,
    work_hours_assigned TEXT,
    project_code TEXT,
    project_description TEXT,
    senior_name TEXT,
    approx_duration INTEGER,
    start_date TEXT,
    end_date TEXT,
    status TEXT
)
""")
