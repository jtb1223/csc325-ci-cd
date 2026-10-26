from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"status": "ok"})


class TaskApiTests(APITestCase):
    def test_create_task(self):
        response = self.client.post(
            reverse("task-list"), {"title": "Write CI pipeline"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertFalse(response.json()["completed"])

    def test_list_tasks(self):
        Task.objects.create(title="First")
        Task.objects.create(title="Second", completed=True)
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([t["title"] for t in response.json()], ["First", "Second"])

    def test_create_task_requires_title(self):
        response = self.client.post(reverse("task-list"), {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
