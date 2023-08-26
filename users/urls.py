
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.views import UserRegistrationView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),
         name='register'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

              ]
