from django.db import models
from config.settings import AUTH_USER_MODEL, NULLABLE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField


class Habit(models.Model):
    """Модель привычки"""


    class Frequency(models.TextChoices):
        DAILY = "DAILY", "Ежедневно"
        WEEKLY = "WEEKLY", "По дням недели"

    class WeekDays(models.IntegerChoices):
        MONDAY = 1, "Понедельник"
        TUESDAY = 2, "Вторник"
        WEDNESDAY = 3, "Среда"
        THURSDAY = 4, "Четверг"
        FRIDAY = 5, "Пятница"
        SATURDAY = 6, "Суббота"
        SUNDAY = 7, "Воскресенье"

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
    # period = models.PositiveSmallIntegerField(
    #     default=1,
    #     verbose_name='Периодичность',
    #     help_text='Периодичность выполнения привычки для напоминания в днях',
    #     # validators=[MinValueValidator(1), MaxValueValidator(7)],
    #     **NULLABLE,
    # )
    frequency_type = models.CharField(
        max_length=10,
        choices=Frequency.choices,
        default=Frequency.DAILY,
        verbose_name="Тип периодичности",

    )
    weekdays = ArrayField(
        models.PositiveSmallIntegerField(choices=WeekDays.choices),
        blank=True,
        null=True,
        verbose_name="Дни недели",
        help_text="Если выбрано 'По дням недели', укажите дни выполнения",
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
    # habit_start = models.DateField(
    #
    #     verbose_name='Дата начала работы с привычкой',
    #     help_text='Укажите дату начала вырабатывания привычки',
    #     **NULLABLE,
    # )
    is_reminder_send = models.BooleanField(
        default=False,
        verbose_name='Флаг, что напоминание отправлено',
        **NULLABLE,
    )

    def __str__(self):
        # return f'{self.action} в {self.habit_time} в {self.place}'
        return (
            f"{'Приятная' if self.is_enjoyed else 'Полезная'} привычка: {self.action}"
        )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
