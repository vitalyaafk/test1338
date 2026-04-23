import sqlite3
def get_conection():
    return sqlite3.connect("users.db")
def create_table():
    conn = get_conection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL)""")
    conn.commit()
    conn.close()