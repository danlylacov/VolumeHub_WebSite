from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='Confirm password')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'telegram_id', 'subscription')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            telegram_id=validated_data['telegram_id'],
            subscription=validated_data['subscription']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user