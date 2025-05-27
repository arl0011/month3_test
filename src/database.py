import sqlite3

class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    note TEXT
                )
            """)

    def all_contacts(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM contacts")
            return result.fetchall()

    def add_contact(self, name: str, phone: str, note: str):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT INTO contacts (name, phone, note) VALUES (?, ?, ?)",
                (name, phone, note)
            )
            conn.commit()

    def delete_contact(self, contact_id: int):
        with sqlite3.connect(self.path) as conn:
            conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
            conn.commit()
