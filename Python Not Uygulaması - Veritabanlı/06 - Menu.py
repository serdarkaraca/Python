while True:
    print("\n1. Not Ekle\n2. Notları Görüntüle\n3. Not Sil\n4. Çıkış")
    secim = input("Seçiminiz: ")

    if secim == '1':
        baslik = input("Not Başlığı: ")
        icerik = input("Not İçeriği: ")
        not_ekle(baslik, icerik)
    elif secim == '2':
        notlari_goster()
    elif secim == '3':
        id = input("Silmek istediğiniz notun ID’si: ")
        not_sil(id)
    elif secim == '4':
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")
