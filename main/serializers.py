from rest_framework import serializers
from main.models import Habit
from main.validators import (HabitLengthValidator,
                             HabitRewardValidator,
                             HabitPleasantValidator,
                             HabitPeriodityValidator)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitLengthValidator(field='length'),
                      HabitRewardValidator(),
                      HabitPleasantValidator(),
                      HabitPeriodityValidator()]
