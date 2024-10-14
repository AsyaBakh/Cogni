from django.urls import include
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login.as_view(), name='login'),
    path('', include('cogniReact.urls')),
]
