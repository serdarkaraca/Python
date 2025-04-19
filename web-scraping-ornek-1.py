import requests
from bs4 import BeautifulSoup

# İlgili URL
url = "https://serdarkaraca.com.tr"

# HTTP isteği gönder
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Başlıkları bul
headlines = soup.find_all("h4")

print("serdarkaraca.com.tr'de Yazı Başlıkları :")
for h in headlines:
    print("-", h.text.strip())
