from datetime import datetime

from celery import shared_task
from django.utils.timezone import now
from requests import RequestException

from habits.models import Habit
from habits.servises import send_telegram_message


@shared_task
def time():
    current_time = now().time()
    current_date = now().date()
    current_weekday = current_date.weekday() + 1
    print(current_time)


@shared_task(
    autoretry_for=(RequestException,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def send_habit_reminder():

    dt_time = datetime.now()
    current_time = dt_time.time()
    current_weekday = dt_time.weekday() + 1

    daily_habits = Habit.objects.select_related("owner").filter(
        frequency_type=Habit.Frequency.DAILY,
        is_enjoyed=False,
        owner__tg_chat_id__isnull=False,
    )
    for habit in daily_habits:
        if habit.habit_time > current_time:
            user = habit.owner
            tg_chat = user.tg_chat_id
            message = f"Я буду {habit.action} в {habit.habit_time} в {habit.place}."
            send_telegram_message(
                tg_chat, message
            )  # Отправляем привычку в Telegram чат

    weekly_habits = Habit.objects.select_related("owner").filter(
        frequency_type=Habit.Frequency.WEEKLY,
        is_enjoyed=False,
        owner__tg_chat_id__isnull=False,
    )
    for habit in weekly_habits:
        if (
            current_weekday in (habit.weekdays or [])
            and habit.habit_time > current_time
        ):
            user = habit.owner
            tg_chat = user.tg_chat_id
            message = f"Я буду {habit.action} в {habit.habit_time} в {habit.place}."
            send_telegram_message(
                tg_chat, message
            )  # Отправляем привычку в Telegram чат
