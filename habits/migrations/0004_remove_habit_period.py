# Generated by Django 5.1.4 on 2024-12-18 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_habit_frequency_type_habit_weekdays_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="period",
        ),
    ]
