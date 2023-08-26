from django.urls import path

from rest_framework.routers import DefaultRouter
from main.views import (HabitViewSet,
                        PublicHabitListAPIView,
                        PersonalHabitListAPIView)

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

app_name = 'main'
urlpatterns = [
            path('public/', PublicHabitListAPIView.as_view(),
                 name="public_habits"),
            path('personal/', PersonalHabitListAPIView.as_view(),
                 name="personal_habits"),

              ] + router.urls
