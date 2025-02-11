from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from todo.models import Task


class ModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(content='Test',is_done=True)

    def test_task_list_view(self) -> None:
        url = reverse("todo:tasks_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_tag_list_view(self) -> None:
        url = reverse("todo:tags_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        ulr = reverse("todo:task_form")
        data = {
            "content": "TestTask",
            "is_done": False,
        }
        response = self.client.post(ulr, data)
        self.assertEqual(response.status_code, 302)

    def test_task_update(self):
        url = reverse("todo:task_update", kwargs={"pk": self.task.pk})
        data = {"content": "Test",
                "is_done": True,
                }
        response = self.client.post(
            url,
            content_type="application/json",
            data=data)

        self.assertEqual(response.status_code, 200)

    def test_task_delete(self):
        url = reverse("todo:task_delete", kwargs={"pk": self.task.pk})
        data = {"content": "Test",
                "is_done": False,
                }
        response = self.client.post(
            url,
            content_type="application/json",
            data=data
        )

        self.assertEqual(response.status_code, 302)