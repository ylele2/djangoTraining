from django.contrib.auth.models import User
from rest_framework import serializers
from .models import APIKey, BotSettings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['api_key', 'api_secret']

class BotSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotSettings
        fields = ['crypto', 'profit_margin', 'pyramiding_level', 'rebuy_option', 'is_active']
