import json

kisi = {
    "ad": "Ayşe",
    "soyad": "Yılmaz",
    "yas": 28,
    "meslek": "Veri Analisti"
}

with open("kisi.json", "w", encoding="utf-8") as dosya:
    json.dump(kisi, dosya, ensure_ascii=False, indent=4)
