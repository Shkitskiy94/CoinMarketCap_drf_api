from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import User
from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    """Отображение кастомного юзера"""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
