from app.sql_db import conn, c


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def insert_data(self, data):
        # insert data into the storage column
        c.execute("UPDATE users SET storage = ? WHERE user = ?", (data, self.username))
        conn.commit()

    def delete_data(self):
        # delete data from the storage
        c.execute("UPDATE users SET storage = NULL WHERE user = ?", (self.username,))
        conn.commit()

    def view_saved_data(self):
        # retrieve data from the storage
        c.execute("SELECT storage FROM users WHERE user = ?", (self.username,))
        result = c.fetchone()
        if result and result[0]:
            return result[0]
        else:
            return "No saved data."
