import sqlite3

def get_connection():
    return sqlite3.connect("scattersense.db")

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY AUTOINCREMENT, session_date TEXT, time_period TEXT, duration INTEGER, energy_level TEXT, task_type TEXT)"
    )
    connection.commit()
    connection.close()

def insert_session(session_date, time_period, duration, energy_level, task_type):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO sessions (session_date, time_period, duration, energy_level, task_type) VALUES (?, ?, ?, ?, ?)",
        (session_date, time_period, duration, energy_level, task_type)
    )
    connection.commit()
    connection.close()

def fetch_sessions():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, session_date, time_period, duration, energy_level, task_type FROM sessions ORDER BY id DESC"
    )
    rows = cursor.fetchall()
    connection.close()
    return rows

def fetch_filtered_sessions(date_from=None, date_to=None, task_search=None, energy_filter=None):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT id, session_date, time_period, duration, energy_level, task_type FROM sessions WHERE 1=1"
    params = []

    if date_from:
        query += " AND session_date >= ?"
        params.append(date_from)
    if date_to:
        query += " AND session_date <= ?"
        params.append(date_to)
    if task_search:
        query += " AND task_type LIKE ?"
        params.append(f"%{task_search}%")
    if energy_filter:
        query += " AND energy_level = ?"
        params.append(energy_filter)

    query += " ORDER BY id DESC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete_session(session_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM sessions WHERE id = ?",
        (session_id,)
    )
    connection.commit()
    connection.close()
