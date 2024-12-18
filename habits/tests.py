from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from habits.models import Habit
from users.models import CustomUser


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="user1@habits.ru", password="123456789", username="user1"
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            place="на улице",
            habit_time="12:00:00",
            action="бег",
            lead_time="60",
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_retrieve(self):
        """тест создание привычки"""
        # url = reverse("habits:habit_retrieve", args=(self.habit.pk,))
        url = f"/habits/{self.habit.pk}/detail/"
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)


class PublicHabitListAPIViewTest(APITestCase):
    def setUp(self):
        self.test_user1 = CustomUser.objects.create(
            email="user1@habits.ru", username="user1", password="12345678"
        )
        self.client = APIClient()

        self.public_habit = Habit.objects.create(
            owner=self.test_user1,
            place="Стадион Орбита",
            habit_time="06:00:00",
            action="Бег",
            is_enjoyed=True,
            lead_time=30,
            is_published=True,
            frequency_type="DAILY",
        )

        self.private_habit = Habit.objects.create(
            owner=self.test_user1,
            place="Дом",
            habit_time="20:00:00",
            action="Чтение книг",
            is_enjoyed=False,
            lead_time=45,
            is_published=False,
            frequency_type="DAILY",
        )

    def test_public_habit_list(self):
        """Тест на список публичных привычек"""
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.get("/habits/published/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)


class HabitValidationTestCase(APITestCase):
    def setUp(self):
        self.test_user1 = CustomUser.objects.create(
            username="test_user1", password="12345678"
        )
        self.client = APIClient()

        self.related_habit = Habit.objects.create(
            owner=self.test_user1,
            place="Дом",
            habit_time="08:00:00",
            action="Читать книгу",
            is_enjoyed=True,
            lead_time=60,
            is_published=True,
            frequency_type="DAILY",
            prize=None,
            habit_link=None,
        )

        self.incorrect_data1 = {
            "place": "Парк",
            "habit_time": "08:30:00",
            "action": "Прогулка",
            "is_enjoyed": False,
            "lead_time": 60,
            "is_published": True,
            "frequency_type": "DAILY",
            "weekdays": None,
            "prize": "Выпить кофе",
            "habit_link": self.related_habit.id,
        }

        self.incorrect_data2 = {
            "place": "Парк",
            "habit_time": "08:30:00",
            "action": "Прогулка",
            "is_enjoyed": False,
            "lead_time": 125,
            "is_published": True,
            "frequency_type": "DAILY",
            "weekdays": None,
            "prize": "Выпить кофе",
            "habit_link": None,
        }

        self.incorrect_data3 = {
            "place": "Парк",
            "habit_time": "08:30:00",
            "action": "Прогулка",
            "is_enjoyed": False,
            "lead_time": 60,
            "is_published": True,
            "frequency_type": "WEEKLY",
            "weekdays": [],
            "prize": "Выпить кофе",
            "habit_link": None,
        }

        self.incorrect_data4 = {
            "place": "Парк",
            "habit_time": "08:30:00",
            "action": "Прогулка",
            "is_enjoyed": False,
            "lead_time": 60,
            "is_published": True,
            "frequency_type": "DAILY",
            "weekdays": [1],
            "prize": "Выпить кофе",
            "habit_link": None,
        }

    def test_create_habit_with_reward_and_related_habit(self):
        """Тест на ошибку при указании одновременно вознаграждения и связанной привычки"""
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.post(
            "/habits/create/", self.incorrect_data1, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Вознаграждение и связанная привычка не могут быть одновременно указаны",
            str(response.data),
        )

    def test_create_habit_with_duration_more_than_120(self):
        """Тест на ошибку при времени выполнения больше 120 секунд"""
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.post(
            "/habits/create/", self.incorrect_data2, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Ensure this value is less than or equal to 120.", str(response.data)
        )

    def test_create_habit_with_no_weekdays_for_weekly(self):
        """Тест на ошибку при отсутствии дней недели для недельной привычки"""
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.post(
            "/habits/create/", self.incorrect_data3, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Привычка должна выполняться хотя бы раз в 7 дней. Укажите дни недели",
            str(response.data),
        )

    def test_create_habit_with_weekdays_for_daily(self):
        """Тест на ошибку при указании дней недели для ежедневной привычки"""
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.post(
            "/habits/create/", self.incorrect_data4, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
