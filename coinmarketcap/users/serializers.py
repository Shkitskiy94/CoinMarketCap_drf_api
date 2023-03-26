from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import User


class CustomUserSerializer(UserSerializer):
    """Serializer пользователя"""
    class Meta:
        model = User
        fields = (
            'username',
            'id',
            'email',
            'first_name',
            'last_name',)


class CustomUserCreateSerializer(UserCreateSerializer):
    """Serializer создания пользователя"""
    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password'  
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        if not validated_data['email']:
            raise ValueError("укажите email")
        user = User.objects.create(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user
