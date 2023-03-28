from django.urls import reverse_lazy
from django.views.generic import CreateView
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .forms import CreationForm
from .models import User
from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    """Отображение кастомного юзера"""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('crypto:home')
    template_name = 'users/signup.html'
