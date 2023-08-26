import json
from datetime import datetime
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import viewsets, generics
from main.models import Habit
from main.paginators import MaterialPaginator
from main.permissions import IsOwner
from main.serializers import HabitSerializer


# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    '''ViewSet для модели  Привычка'''
    serializer_class = HabitSerializer
    pagination_class = MaterialPaginator
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        public_habits = Habit.objects.filter(is_public=True)
        user_habits = Habit.objects.filter(owner=user)
        queryset = public_habits | user_habits
        queryset = self.filter_queryset(queryset)
        return queryset

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()

        if new_habit.periodity == 'daily':
            interval = IntervalSchedule.objects.create(
                every=1,
                period=IntervalSchedule.DAYS
            )
        elif new_habit.periodity == 'weekly':
            interval = IntervalSchedule.objects.create(
                every=7,
                period=IntervalSchedule.DAYS
            )

        habit_time = new_habit.time
        start_time = datetime.combine(datetime.now(), habit_time)
        PeriodicTask.objects.create(
            interval=interval,
            name=new_habit.id,
            task='main.tasks.send_to_bot',
            start_time=start_time,
            args=json.dumps([str(new_habit.id)])

        )


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)


class PersonalHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)
