from django.test import TestCase
from django.urls import reverse


class HelloViewTests(TestCase):
    def test_root_says_hello(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello, World!")
