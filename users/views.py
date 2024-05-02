from rest_framework import generics
from django.contrib.auth import get_user_model
from users import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password


User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [~IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        raw_password = serializer.validated_data.get("password")
        password = make_password(raw_password)
        serializer.save(password=password)


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
