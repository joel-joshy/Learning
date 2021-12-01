from django.urls import path
from .views import VerifyEmail, RegistrationView, LoginAPIView, LogoutView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('email-verify', VerifyEmail.as_view(), name='email-verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='logout')
]
