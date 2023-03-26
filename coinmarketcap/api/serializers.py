from .models import Cryptocurrency, Favorite
from rest_framework import serializers


class CryptocurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ('id', 'symbol', 'name', 'price',
                  'change_24h', 'volume_24h')


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ('id', 'symbol', 'name', 'price',
                  'change_24h', 'volume_24h')


class FavoriteSerializer(serializers.ModelSerializer):
    """Serializer для избранных криптовалют"""

    def validate(self, data):
        request = self.context.get('request')
        crypto = data['crypto']
        if Favorite.objects.filter(user=request.user, crypto=crypto).exists():
            raise serializers.ValidationError({
                'status': 'криптовалюта уже есть в избранном'
            })
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return CryptocurrencySerializer(
            instance.crypto, context=context).data

    class Meta:
        model = Favorite
        fields = ('user', 'crypto')


class NewsSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    url = serializers.URLField()
