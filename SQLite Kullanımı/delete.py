import sqlite3

conn = sqlite3.connect("veritabanim.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM ogrenciler WHERE ad = ?", ("Serdar",))

conn.commit()
conn.close()
