from rest_framework.serializers import ModelSerializer
from habits.models import Habit
from habits.validators import RewardAndRelatedValidator, RelatedAndIsGoodValidator, FrequencyValidator


class HabitSerializer(ModelSerializer):
    """Сериализатор для привычки"""

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardAndRelatedValidator(),
            RelatedAndIsGoodValidator(),
            FrequencyValidator(),
        ]
