import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
table_exists = c.fetchone()

if not table_exists:
    # create 'users' table with columns
    c.execute(
        """
        CREATE TABLE users (
            user TEXT,
            password TEXT,
            storage TEXT
        )
        """
    )

conn.commit()
