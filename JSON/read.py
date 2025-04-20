import json

with open("veri.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)

print(veri)
print(veri["ad"])
