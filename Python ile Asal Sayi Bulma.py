def asal_mi(sayi):
    if sayi <= 1:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Kullanıcıdan giriş alınır
try:
    girilen_sayi = int(input("Bir sayı girin: "))
    if asal_mi(girilen_sayi):
        print(f"{girilen_sayi} bir asal sayıdır.")
    else:
        print(f"{girilen_sayi} asal bir sayı değildir.")
except ValueError:
    print("Lütfen geçerli bir tam sayı girin.")
