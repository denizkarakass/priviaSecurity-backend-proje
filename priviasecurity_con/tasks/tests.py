from django.test import TestCase

import requests

data = {
    "id": "00001",
    "name": "DevOps",
    "completedPercent": 0
}

url = "http://127.0.0.1:8000/tasks/create"

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Veri başarıyla eklendi.")
else:
    print("Bir hata oluştu. İsteğiniz gerçekleştirilemedi.")
