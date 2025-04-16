# Vize-Final Ortalaması Hesaplama Programı

print("Vize-Final Ortalaması Hesaplama Programına Hoş Geldiniz!")

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))

ortalama = (vize * 0.4) + (final * 0.6)

print(f"Ortalamanız: {ortalama:.2f}")

if ortalama >= 60:
    print("Tebrikler, dersten geçtiniz! ")
else:
    print("Üzgünüz, dersten kaldınız. ")
