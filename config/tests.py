from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):
    def test_homepage_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)