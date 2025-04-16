def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Bir sayı sıfıra bölünemez!"
    return x / y

print("İşlem Seçiniz:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi yapınız (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

if secim == '1':
    print("Sonuç:", toplama(sayi1, sayi2))
elif secim == '2':
    print("Sonuç:", cikarma(sayi1, sayi2))
elif secim == '3':
    print("Sonuç:", carpma(sayi1, sayi2))
elif secim == '4':
    print("Sonuç:", bolme(sayi1, sayi2))
else:
    print("Geçersiz seçim!")
