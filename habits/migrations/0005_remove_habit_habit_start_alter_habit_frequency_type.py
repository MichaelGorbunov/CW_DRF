# Generated by Django 5.1.4 on 2024-12-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_remove_habit_period"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="habit_start",
        ),
        migrations.AlterField(
            model_name="habit",
            name="frequency_type",
            field=models.CharField(
                choices=[("DAILY", "Ежедневно"), ("WEEKLY", "По дням недели")],
                default="DAILY",
                max_length=10,
                verbose_name="Тип периодичности",
            ),
        ),
    ]
