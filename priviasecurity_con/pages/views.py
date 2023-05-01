import requests
import requests_mock

from django.shortcuts import render

def index(request):
    with requests_mock.Mocker() as mock:
        mock.get('http://example.com', text='mocked response')

        response = requests.get('http://example.com')
        assert response.status_code == 200
        assert response.text == 'mocked response'
    print(response.status_code)
    return render(request, 'index.html')
