import sqlite3

conn = sqlite3.connect('notlar.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS notlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    baslik TEXT NOT NULL,
    icerik TEXT NOT NULL
)
''')

conn.commit()
conn.close()
