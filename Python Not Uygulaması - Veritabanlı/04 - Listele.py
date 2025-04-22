def notlari_goster():
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notlar")
    notlar = cursor.fetchall()
    for not_ in notlar:
        print(f"{not_[0]} - {not_[1]}: {not_[2]}")
    conn.close()
