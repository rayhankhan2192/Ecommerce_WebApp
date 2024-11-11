from django.urls import path

from .views import UserRegistrationViews

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='user-registration'),
]