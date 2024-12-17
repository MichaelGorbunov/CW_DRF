from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import CustomUser
from users.permissions import IsAccountOwner
from users.serializer import (CustomUserDetailSerializer, CustomUserSerializer)

class CustomUserViewSet(viewsets.ModelViewSet):
    """viewset модели customuser"""

    # serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]  # Пзволяем создавать пользователей без авторизации


    def get_permissions(self):
        # Получаем список разрешений, в зависимости от типа запроса
        if self.action in ["create"]:  # Если действие - создание пользователя
            permission_classes = [AllowAny]  # Позволяем всем доступ к этому действию
        else:  # Для остальных действий (retrieve, update, delete и т.д.)
            # permission_classes = [permissions.IsAuthenticated]  # Требуем аутентификацию
            self.permission_classes = [IsAccountOwner]

        # return [permission() for permission in permission_classes]
        return super().get_permissions()

    def perform_create(self, serializer):
        # Создаем пользователя с указанными данными и устанавливаем активность
        user = serializer.save(is_active=True)
        # Устанавливаем хешированный пароль
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        # if self.action in ["retrieve", "update", "partial_update"]:

        # user = self.get_object()
        # if self.request.user == user:
        if self.request.user.user_permissions == IsAccountOwner:
            return CustomUserDetailSerializer  # Если пользователь владелец, используем полный сериализатор
        else:
            return CustomUserSerializer  # В противном случае - ограниченный
