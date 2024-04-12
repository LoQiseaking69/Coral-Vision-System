
import sqlite3

def setup_database():
    connection = sqlite3.connect('inferences.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY,
        datetime TEXT,
        inference TEXT
    )
    ''')
    connection.commit()
    connection.close()

if __name__ == "__main__":
    setup_database()
