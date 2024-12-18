# import requests
from celery import shared_task
from django.utils.timezone import now
from requests import RequestException

from habits.models import Habit
from habits.servises import send_telegram_message


# @shared_task(
#     autoretry_for=(RequestException,),
#     retry_backoff=True,
#     retry_kwargs={'max_retries': 5},
# )
def check_habits():
    """Проверяет привычки и отправляет сообщение, если подходит время их выполнения"""
    current_time = now().time()
    current_date = now().date()
    current_weekday = current_date.weekday() + 1

    current_hour = current_time.hour
    current_minute = current_time.minute

    habits = Habit.objects.select_related('owner').filter(
        is_enjoyed=False, owner__tg_chat_id__isnull=False
    )

    daily_habits = habits.filter(
        frequency_type=Habit.Frequency.DAILY, is_enjoyed=False
    )
    # for habit in daily_habits:
    #     habit_hour = habit.habit_time.hour
    #     habit_minute = habit.habit_time.minute
    #
    #     if habit_hour == current_hour and habit_minute == current_minute:
    #         message = f"Я буду {habit.action} в {habit.habit_time.strftime('%H:%M')} в {habit.place}"
    #         if habit.owner.tg_chat_id:
    #             send_telegram_message(message, habit.owner.tg_chat_id)
    for habit in daily_habits:
        message = f"Я буду {habit.action} в {habit.habit_time.strftime('%H:%M')} в {habit.place}"
        send_telegram_message(message, habit.owner.tg_chat_id)

    weekly_habits = habits.filter(
        frequency_type=Habit.Frequency.WEEKLY, is_enjoyed=False
    )
    # for habit in weekly_habits:
    #     habit_hour = habit.habit_time.hour
    #     habit_minute = habit.habit_time.minute
    #
    #     if (
    #             current_weekday in (habit.weekdays or [])
    #             and habit_hour == current_hour
    #             and habit_minute == current_minute
    #     ):
    #         message = f"Я буду {habit.action} в {habit.time.strftime('%H:%M')} в {habit.place}"
    #         if habit.user.tg_chat_id:
    #             send_telegram_message(message, habit.owner.tg_chat_id)
    for habit in weekly_habits:
        message = f"Я буду {habit.action} в {habit.habit_time.strftime('%H:%M')} в {habit.place}"
        send_telegram_message(message, habit.owner.tg_chat_id)