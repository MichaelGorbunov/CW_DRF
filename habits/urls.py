from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitPublishedListAPIView,
                          HabitRetrieveAPIView, HabitUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    # вывод списка привычек
    path("list/", HabitListAPIView.as_view(), name="habits-list"),
    # вывод списка публичных привычек
    path("published/", HabitPublishedListAPIView.as_view(), name="habits-published"),
    # просмотр одной привычки
    path("<int:pk>/detail/", HabitRetrieveAPIView.as_view(), name="habits-retrieve"),
    # создание привычки
    path("create/", HabitCreateAPIView.as_view(), name="habits-create"),
    # изменение одной привычки
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits-update"),
    # удаление одной привычки
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits-delete"),
]
