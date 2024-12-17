from rest_framework.serializers import ValidationError


class RewardAndRelatedValidator:
    """Исключение одновременного выбора связанной привычки и вознаграждения"""

    def __call__(self, habit):
            if habit.get('habit_link') and habit.get('prize'):
                raise ValidationError('Вознаграждение и связанная привычка не могут быть одновременно указаны')