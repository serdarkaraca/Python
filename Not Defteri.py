import os

NOTLAR_DIZINI = "C:\\PythonTest"

if not os.path.exists(NOTLAR_DIZINI):
    os.mkdir(NOTLAR_DIZINI)

def not_ekle():
    baslik = input("Not başlığı: ")
    icerik = input("Not içeriği: ")
    dosya_yolu = os.path.join(NOTLAR_DIZINI, f"{baslik}.txt")
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        dosya.write(icerik)
    print("Not kaydedildi.")

def notlari_listele():
    notlar = os.listdir(NOTLAR_DIZINI)
    if notlar:
        print("Mevcut Notlar:")
        for not_adi in notlar:
            print("- " + not_adi.replace(".txt", ""))
    else:
        print("Henüz not yok.")

def not_goruntule():
    baslik = input("Görüntülemek istediğiniz notun başlığı: ")
    dosya_yolu = os.path.join(NOTLAR_DIZINI, f"{baslik}.txt")
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            print("\n" + dosya.read())
    else:
        print("Not bulunamadı.")

def not_sil():
    baslik = input("Silmek istediğiniz notun başlığı: ")
    dosya_yolu = os.path.join(NOTLAR_DIZINI, f"{baslik}.txt")
    if os.path.exists(dosya_yolu):
        os.remove(dosya_yolu)
        print("Not silindi.")
    else:
        print("Not bulunamadı.")

def menu():
    while True:
        print("\n--- Python Not Defteri ---")
        print("1. Not Ekle")
        print("2. Notları Listele")
        print("3. Not Görüntüle")
        print("4. Not Sil")
        print("5. Çıkış")

        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_listele()
        elif secim == "3":
            not_goruntule()
        elif secim == "4":
            not_sil()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

menu()
