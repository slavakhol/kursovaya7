from django.conf import settings
from django.db import models


# Create your models here.
class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              null=True, blank=True)
    place = models.CharField(max_length=100, verbose_name="место")
    time = models.TimeField(verbose_name="время")
    periodity = models.CharField(max_length=50,
                                 choices=[('daily', 'Ежедневно'),
                                          ('weekly', 'Еженедельно'),
                                          ('monthly', 'Ежемесячно')]
                                 )
    action = models.CharField(max_length=100, verbose_name="действие")
    length = models.IntegerField(verbose_name="продолжительность в секундах")
    reward = models.CharField(max_length=100,
                              null=True, blank=True,
                              verbose_name="вознаграждение")
    linked_habit = models.ForeignKey('self',
                                     on_delete=models.CASCADE,
                                     null=True, blank=True)
    is_pleasant = models.BooleanField(default=False, verbose_name="приятная?")
    is_public = models.BooleanField(default=True, verbose_name="публичная?")

    def __str__(self):
        return f"{self.owner} будет {self.action}  в {self.time} {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
        ordering = ['owner']
