import sqlite3

conn = sqlite3.connect("veritabanim.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO ogrenciler (ad, soyad, yas) VALUES (?, ?, ?)", 
               ("Serdar", "Karaca", 26))

conn.commit()
conn.close()
