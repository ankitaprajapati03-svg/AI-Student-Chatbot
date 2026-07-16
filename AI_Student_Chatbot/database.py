import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (

id INTEGER PRIMARY KEY AUTOINCREMENT,

question TEXT,

response TEXT,

date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

connection.commit()

connection.close()

print("Database created successfully!")