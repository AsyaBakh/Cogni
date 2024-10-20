from django.urls import path
from .views import register, LoginView

urlpatterns = [
    path('register/', register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='LoginView'),
]