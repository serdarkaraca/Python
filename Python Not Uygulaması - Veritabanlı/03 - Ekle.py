def not_ekle(baslik, icerik):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notlar (baslik, icerik) VALUES (?, ?)", (baslik, icerik))
    conn.commit()
    conn.close()
