from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import APIKey, BotSettings
from .serializers import UserSerializer, APIKeySerializer, BotSettingsSerializer

# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class APIKeyView(generics.RetrieveUpdateAPIView):
    serializer_class = APIKeySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return APIKey.objects.get_or_create(user=self.request.user)[0]


class BotSettingsView(generics.ListCreateAPIView):
    serializer_class = BotSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BotSettings.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
