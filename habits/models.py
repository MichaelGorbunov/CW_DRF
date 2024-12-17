from django.db import models
from config.settings import AUTH_USER_MODEL, NULLABLE
from django.core.validators import MaxValueValidator, MinValueValidator


class Habit(models.Model):
    """Модель привычки"""
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки', **NULLABLE)
    place = models.CharField(
        max_length=150,
        verbose_name='Место',
        help_text='Место, в котором необходимо выполнять привычку',
    )
    habit_time = models.TimeField(
        verbose_name='Время',
        help_text='Время, когда необходимо выполнять привычку',
    )
    action = models.CharField(
        max_length=150,
        verbose_name='Действие',
        help_text='Действие, которое представляет собой привычка',
    )
    is_enjoyed = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки',
        help_text='Укажите, является ли привычка приятной',
    )
    habit_link = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Связанная привычка',
        help_text='Привычка, которая связана с этой привычкой',
        **NULLABLE,
    )
    period = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Периодичность',
        help_text='Периодичность выполнения привычки для напоминания в днях',
        validators=[MinValueValidator(1), MaxValueValidator(7)],
    )
    prize = models.CharField(
        max_length=150,
        verbose_name='Вознаграждение',
        help_text='Чем пользователь должен себя вознаградить после выполнения',
        **NULLABLE,
    )
    lead_time = models.PositiveSmallIntegerField(
        default=30,
        verbose_name='Время на выполнение',
        help_text='Время, которое предположительно потратится на выполнение привычки в секундах',
        validators=[MinValueValidator(10), MaxValueValidator(120)],
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Признак публичности',
        help_text='Привычки можно публиковать в общий доступ',
    )
    habit_start = models.DateField(

        verbose_name='Дата начала работы с привычкой',
        help_text='Укажите дату начала вырабатывания привычки',
        **NULLABLE,
    )
    is_reminder_send = models.BooleanField(
        default=False,
        verbose_name='Флаг, что напоминание отправлено',
        **NULLABLE,
    )

    def __str__(self):
        return f'{self.action} в {self.habit_time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'