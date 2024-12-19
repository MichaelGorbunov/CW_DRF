from rest_framework.serializers import ValidationError

from habits.models import Habit


class RewardAndRelatedValidator:
    """Исключение одновременного выбора связанной привычки и вознаграждения"""

    def __call__(self, habit):
        if habit.get("habit_link") and habit.get("prize"):
            raise ValidationError(
                "Вознаграждение и связанная привычка не могут быть одновременно указаны"
            )


class RelatedAndIsGoodValidator:
    """Проверка связанной привычки и признания ее приятной"""

    def __call__(self, habit):
        celected_habit = habit.get("habit_link")
        if celected_habit:
            if not celected_habit.is_enjoyed:
                raise ValidationError("Связанная привычка должна быть приятной")


class FrequencyValidator:
    """Проверка выполнения привычки 1 или более раз в неделю"""

    def __call__(self, habit):
        frequency_type = habit.get("frequency_type")
        weekdays = habit.get("weekdays")
        if frequency_type == Habit.Frequency.WEEKLY:
            if not weekdays or len(weekdays) < 1:
                raise ValidationError(
                    {
                        "weekdays": "Привычка должна выполняться хотя бы раз в 7 дней. Укажите дни недели"
                    }
                )
        elif frequency_type == Habit.Frequency.DAILY and weekdays is not None:

            raise ValidationError(
                {"weekdays": "Для ежедневной привычки дни недели не указываются"}
            )
