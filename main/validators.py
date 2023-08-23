from rest_framework.serializers import ValidationError

from main.models import Habit


class HabitLengthValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        value = dict(value).get(self.field)
        if value > 120:
            raise ValidationError("Продолжительность слишком длинная")


class HabitRewardValidator:
    def __call__(self, value):
        if value.get('reward') and value.get('linked_habit') is not None:
                raise ValidationError("Нужно указать либо вознаграждение, либо связанную привычку")


class HabitPleasantValidator:
    def __call__(self, value):
        linked_habit = value.get('linked_habit')
        if linked_habit and not linked_habit.is_pleasant:
                raise ValidationError("Связанная привычка не является приятной")
        if value.get('is_pleasant') and value.get('reward'):
                raise ValidationError("У приятной привычки не должно быть вознаграждения")
        if value.get('is_pleasant') and value.get('linked_habit'):
                raise ValidationError("У приятной привычки не должно быть связанной привычки")

class HabitPeriodityValidator:
    def __call__(self, value):
        if value.get('periodity') == "monthly":
                raise ValidationError("Привычка реже недельной")