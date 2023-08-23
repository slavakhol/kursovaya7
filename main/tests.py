from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from main.models import Habit
from users.models import User

# Create your tests here.

class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@email.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания Привычки"""
        data = {
            "place": "Работа",
            "action": "Зарядка",
            "time": "10:30:00",
            "periodity": "weekly",
            "length": "100"
        }
        response = self.client.post(
            '/habit/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )