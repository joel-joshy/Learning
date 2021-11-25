from django.urls import path,include
from .views import RegistrationView


urlpatterns = [
    path('register',RegistrationView.as_view(),name='register'),
    # path('email-verification',VerifyEmail.as_view(),name='email-verify'),

]