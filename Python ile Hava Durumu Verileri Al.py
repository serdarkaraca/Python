import requests

def hava_durumu_sorgula(sehir):
    api_key = "BURADA SİZİN APİ KEY OLMALI"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': sehir,
        'appid': api_key,
        'lang': 'tr',
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        print(f"{sehir} için hava durumu:")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Hava: {data['weather'][0]['description']}")
        print(f"Nem: %{data['main']['humidity']}")
        print(f"Rüzgar Hızı: {data['wind']['speed']} m/s")
    else:
        print("Hava durumu bilgisi alınamadı.")

# Örnek kullanım
sehir_adi = input("Şehir adı girin: ")
hava_durumu_sorgula(sehir_adi)


# ----- OpenWeatherMap API Key Alma
#https://openweathermap.org/ adresine gidin.
#Ücretsiz hesap oluşturun.
#“My API keys” bölümünden bir anahtar oluşturun.
#Bu API key'i kod içerisinde kullanacağız.