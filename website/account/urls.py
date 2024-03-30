# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('news/', views.news, name='news'),
    path('api/register/', views.register_user, name='api_register'),
]
