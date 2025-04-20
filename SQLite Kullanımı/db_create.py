import sqlite3

# Veritabanı bağlantısı
conn = sqlite3.connect("veritabanim.db")

# Cursor nesnesi
cursor = conn.cursor()

# Tablo oluşturma
cursor.execute("""
CREATE TABLE IF NOT EXISTS ogrenciler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT,
    soyad TEXT,
    yas INTEGER
)
""")

conn.commit()
conn.close()
