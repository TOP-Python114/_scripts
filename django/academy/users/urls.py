from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserLoginView, UserLogoutView, UserRegistrationView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
