import random

print("Rastgele Sayı Tahmin Oyununa Hoş Geldiniz!")
print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

rastgele_sayi = random.randint(1, 100)
tahmin_sayisi = 0

while True:
    try:
        tahmin = int(input("Tahmininiz: "))
        tahmin_sayisi += 1

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı girin.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı girin.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettiniz!")
            break
    except ValueError:
        print("⚠Lütfen geçerli bir sayı giriniz.")
