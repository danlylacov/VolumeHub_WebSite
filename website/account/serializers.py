from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'telegram_id', 'subscription']  # Укажите все поля, которые нужно сериализовать
        extra_kwargs = {'password': {'write_only': True}}  # Пароль должен быть доступен только для записи