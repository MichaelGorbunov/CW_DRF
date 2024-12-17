from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitListAPIView(ListAPIView):
    """Контроллер вывода списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class HabitCreateAPIView(CreateAPIView):
    """Контроллер создания новой привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """Автоматическая запись пользователя в атрибут owner и даты начала привычки"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()