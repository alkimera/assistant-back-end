import requests

url = 'http://127.0.0.1:5000/predict'

data = {'text': 'Olá, como você está?'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    print(response.text)
else:
    print(response.text)
