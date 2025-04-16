isim = input("Adınızı girin: ")
yas = input("Yaşınızı girin: ")

with open("C:\\PythonDosya\\kullanicilar.txt", "a") as dosya:
    dosya.write(f"{isim} - {yas}\n")

print("Bilgiler başarıyla kaydedildi.")
