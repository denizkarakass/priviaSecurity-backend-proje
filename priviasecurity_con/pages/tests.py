from django.test import TestCase
import requests
import requests_mock

# Mock Servisi çalışıyor mu test ettim.
class MyTestCase(TestCase):
    def test_mock_service(self):
        with requests_mock.Mocker() as mock:
            mock.get('http://example.com', text='mocked response')
            response = requests.get('http://example.com')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'mocked response')
