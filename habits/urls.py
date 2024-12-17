from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (HabitListAPIView,HabitCreateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    # вывод списка привычек
    path("list/", HabitListAPIView.as_view(), name="habits-list"),
# создание привычки
    path("create/", HabitCreateAPIView.as_view(), name="habits-create"),
   ]