import sqlite3

# Veritabanı bağlantısını kur ve tabloyu oluştur
def veritabani_olustur():
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

# Not ekleme fonksiyonu
def not_ekle(baslik, icerik):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notlar (baslik, icerik) VALUES (?, ?)", (baslik, icerik))
    conn.commit()
    conn.close()
    print("Not başarıyla eklendi.")

# Notları listeleme fonksiyonu
def notlari_goster():
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notlar")
    notlar = cursor.fetchall()
    if not notlar:
        print("Henüz kayıtlı not yok.")
    else:
        for not_ in notlar:
            print(f"ID: {not_[0]} | Başlık: {not_[1]} \n📌 İçerik: {not_[2]}\n{'-'*40}")
    conn.close()

# Not silme fonksiyonu
def not_sil(not_id):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notlar WHERE id = ?", (not_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Belirtilen ID'de not bulunamadı.")
    else:
        print("Not başarıyla silindi.")
    conn.close()

# Ana menü
def menu():
    veritabani_olustur()
    while True:
        print("\n🔹 NOT TUTMA UYGULAMASI 🔹")
        print("1. Yeni not ekle")
        print("2. Notları listele")
        print("3. Not sil")
        print("4. Çıkış\n")
        secim = input("Lütfen bir seçenek girin (1-4): ")

        if secim == '1':
            baslik = input("Not başlığı: ")
            icerik = input("Not içeriği: ")
            not_ekle(baslik, icerik)
        elif secim == '2':
            notlari_goster()
        elif secim == '3':
            try:
                not_id = int(input("Silmek istediğiniz notun ID’si: "))
                not_sil(not_id)
            except ValueError:
                print("❗ Geçerli bir sayı girin.")
        elif secim == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-4 arasında bir değer girin.")

# Uygulamayı başlat
if __name__ == '__main__':
    menu()
