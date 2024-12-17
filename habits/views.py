from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListAPIView(ListAPIView):
    """Контроллер вывода списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination


class HabitCreateAPIView(CreateAPIView):
    """Контроллер создания новой привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """Автоматическая запись пользователя в атрибут owner и даты начала привычки"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitPublishedListAPIView(ListAPIView):
    """Контроллер вывода списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = CustomPagination


class HabitRetrieveAPIView(RetrieveAPIView):
    """Контроллер просмотра одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitUpdateAPIView(UpdateAPIView):
    """Контроллер изменения одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    """Контроллер удаления одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)
