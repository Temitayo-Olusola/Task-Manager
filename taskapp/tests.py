from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status

class TaskAPITestCase(APITestCase):
        def setUp(self):
            self.task_detail = {'Title': 'test', 'Description': 'API testing', 'Due_Date': '2023-08-26', 'Completed': 'False'}
            self.task = Task.objects.create(**self.task_detail)

        def test_create_task(self):
            response = self.client.post(self.task_detail, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            

        def test_retrieve_task(self):
            updated_information = {'Title': 'updated task', 'Description': 'api updated', 'due_date': '2023-08-28', 'Completed': 'False'}
            response = self.client.put(updated_information, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.task.refresh_from_db()

        def test_delete_task(self):
            response = self.client.delete()
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)