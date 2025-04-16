def harf_notu_hesapla(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 60:
        return "DC"
    else:
        return "FF"

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6)

print(f"Ortalamanız: {ortalama:.2f}")
print("Harf Notunuz:", harf_notu_hesapla(ortalama))
