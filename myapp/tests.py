from django.test import TestCase
from django.urls import reverse


class HelloViewTests(TestCase):
    def test_root_says_hello(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")

    def test_home_links_to_about(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, f'href="{reverse("about")}"')

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the about page of my Django project")
        self.assertContains(response, "myapp/cow.gif")
