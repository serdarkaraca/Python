import sqlite3

conn = sqlite3.connect("veritabanim.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM ogrenciler")
veriler = cursor.fetchall()

for veri in veriler:
    print(veri)

conn.close()
