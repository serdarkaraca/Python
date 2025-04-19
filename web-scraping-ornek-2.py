import requests
from bs4 import BeautifulSoup

url = "https://serdarkaraca.com.tr/kategori/javascript"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="spnc-post-content")

for product in products:
    name = product.find("h4").text
    description = product.find("p", class_="spnc-description").text
    print(f"Yazı: {name}, Description: {description}")
