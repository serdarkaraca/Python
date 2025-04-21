import requests

url = "https://serdarkaraca.com.tr/demo/json_demo.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for post in data[:5]:  # İlk 5 gönderiyi yazdıralım
        print(f"---------")
        print(f"UserID: {post['userId']}")
        print(f"İsim: {post['title']}")
        print(f"Yaş: {post['yas']}")
        print(f"---------")
else:
    print("API isteği başarısız oldu!")
