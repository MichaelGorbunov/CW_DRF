from rest_framework.serializers import ValidationError


class RewardAndRelatedValidator:
    """Исключение одновременного выбора связанной привычки и вознаграждения"""

    def __call__(self, habit):
        if habit.get('habit_link') and habit.get('prize'):
            raise ValidationError('Вознаграждение и связанная привычка не могут быть одновременно указаны')


class RelatedAndIsGoodValidator:
    """Проверка связанной привычки и признания ее приятной"""

    def __call__(self, habit):
        celected_habit = habit.get('habit_link')
        if celected_habit:
            if not celected_habit.is_enjoyed:
                raise ValidationError('Связанная привычка должна быть приятной')
