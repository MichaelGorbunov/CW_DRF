from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import CustomUser
class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="user1@habits.ru", password='123456789',username="user1")
        self.habit = Habit.objects.create(
            owner=self.user, place="на улице", habit_time="12:00:00", action="бег", lead_time='60'
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_retrieve(self):
        # url = reverse("habits:habit_retrieve", args=(self.habit.pk,))
        url = f"/habits/{self.habit.pk}/detail/"
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)
