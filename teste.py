import requests
import json

url = "http://localhost:8000/api/user-speech/"

data = {"text": "Olá, como vai?"}

response = requests.post(url, json=data)

assert response.status_code == 200, "Status code não é 200"

response_data = response.json()
assert response_data.get("received_text") == data["text"], "Texto recebido não corresponde ao enviado"

print(response_data)
print("Teste concluído com sucesso.")