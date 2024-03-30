# myapp/urls.py
from django.urls import path
from . import views
from .views import UserRegistrationAPIView




urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('signin/', views.signin, name='signin'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='api_signup'),
]



