import requests

# JSON dosyasını URL'den çek
url = 'https://serdarkaraca.com.tr/demo/City_List.json'
response = requests.get(url)

if response.status_code == 200:
    sehirler = response.json()
    turkiye_sehirleri = [s for s in sehirler if s['country'] == 'TR']

    # Sıra numarası ile şehirleri yazdır
    for i, sehir in enumerate(turkiye_sehirleri, start=1):
        print(f"Sıra : {i} - Şehir veya İlçe Adı : {sehir['name']}")
else:
    print("Dosya alınamadı, durum kodu:", response.status_code)
