import sqlite3

conn = sqlite3.connect("veritabanim.db")
cursor = conn.cursor()

cursor.execute("UPDATE ogrenciler SET yas = ? WHERE ad = ?", (25, "Serdar"))

conn.commit()
conn.close()
