from .models import Cryptocurrency
from rest_framework import serializers


class CryptocurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ('id', 'identifier', 'symbol', 'name', 'price',
                  'change_24h', 'volume_24h')


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ('id', 'identifier', 'symbol', 'name', 'price',
                  'change_24h', 'volume_24h')