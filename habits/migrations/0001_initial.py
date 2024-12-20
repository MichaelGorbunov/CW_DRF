# Generated by Django 5.1.4 on 2024-12-17 12:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        help_text="Место, в котором необходимо выполнять привычку",
                        max_length=150,
                        verbose_name="Место",
                    ),
                ),
                (
                    "habit_time",
                    models.TimeField(
                        help_text="Время, когда необходимо выполнять привычку",
                        verbose_name="Время",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        help_text="Действие, которое представляет собой привычка",
                        max_length=150,
                        verbose_name="Действие",
                    ),
                ),
                (
                    "is_enjoyed",
                    models.BooleanField(
                        default=False,
                        help_text="Укажите, является ли привычка приятной",
                        verbose_name="Признак приятной привычки",
                    ),
                ),
                (
                    "period",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="Периодичность выполнения привычки для напоминания в днях",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(7),
                        ],
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "prize",
                    models.CharField(
                        blank=True,
                        help_text="Чем пользователь должен себя вознаградить после выполнения",
                        max_length=150,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "lead_time",
                    models.PositiveSmallIntegerField(
                        default=30,
                        help_text="Время, которое предположительно потратится на выполнение привычки в секундах",
                        validators=[
                            django.core.validators.MinValueValidator(10),
                            django.core.validators.MaxValueValidator(120),
                        ],
                        verbose_name="Время на выполнение",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False,
                        help_text="Привычки можно публиковать в общий доступ",
                        verbose_name="Признак публичности",
                    ),
                ),
                (
                    "habit_start",
                    models.DateField(
                        blank=True,
                        help_text="Укажите дату начала вырабатывания привычки",
                        null=True,
                        verbose_name="Дата начала работы с привычкой",
                    ),
                ),
                (
                    "is_reminder_send",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        null=True,
                        verbose_name="Флаг, что напоминание отправлено",
                    ),
                ),
                (
                    "habit_link",
                    models.ForeignKey(
                        blank=True,
                        help_text="Привычка, которая связана с этой привычкой",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
