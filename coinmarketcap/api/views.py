import json

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .filters import CryptocurrencyFilter
from .models import Cryptocurrency, Favorite
from .serializers import (CryptocurrencySerializer, FavoriteSerializer,
                          NewsSerializer)


def save_cryptocurrencies():
    limit = settings.LIMIT
    start = settings.START
    crypto_api_key = settings.CRYPTO_API_KEY

    response = requests.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
        params={
            'convert': 'USD',
            'start': start,
            'limit': limit
        },
        headers={'Accepts': 'application/json',
                 'X-CMC_PRO_API_KEY': crypto_api_key})

    data = response.json()
    cryptocurrencies = []
    for currency in data['data']:
        id = currency['id']
        symbol = currency['symbol']
        name = currency['name']
        price = currency['quote']['USD']['price']
        change_24h = currency['quote']['USD']['percent_change_24h']
        volume_24h = currency['quote']['USD']['volume_24h']
        cryptocurrency = Cryptocurrency(id=id, symbol=symbol, name=name,
                                        price=price, change_24h=change_24h,
                                        volume_24h=volume_24h)
        cryptocurrency.save()
        json_dict = {'id': id, 'symbol': symbol, 'name': name, 'price': price,
                     'change_24h': change_24h, 'volume_24h': volume_24h}
        cryptocurrencies.append(json_dict)

    while len(data['data']) == limit:
        start += limit
        response = requests.get(
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
            params={
                'convert': 'USD',
                'start': start,
                'limit': limit
            },
            headers={'Accepts': 'application/json',
                     'X-CMC_PRO_API_KEY': crypto_api_key})
        data = response.json()
        for currency in data['data']:
            id = currency['id']
            symbol = currency['symbol']
            name = currency['name']
            price = currency['quote']['USD']['price']
            change_24h = currency['quote']['USD']['percent_change_24h']
            volume_24h = currency['quote']['USD']['volume_24h']
            cryptocurrency = Cryptocurrency(id=id, symbol=symbol, name=name,
                                            price=price, change_24h=change_24h,
                                            volume_24h=volume_24h)
            cryptocurrency.save()
            json_dict = {'id': id, 'symbol': symbol, 'name': name,
                         'price': price, 'change_24h': change_24h,
                         'volume_24h': volume_24h}
            cryptocurrencies.append(json_dict)

    with open('cryptocurrencies.json', 'w') as f:
        json.dump(cryptocurrencies, f)


@api_view(['GET'])
def get(self, *args, **kwargs):
    save_cryptocurrencies()
    return redirect('/api/crypto/')


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    """View представления крипты"""
    queryset = Cryptocurrency.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CryptocurrencyFilter
    serializer_class = CryptocurrencySerializer

    def _post_method_actions(self, request, pk, serializers):
        data = {'user': request.user.id, 'crypto': pk}
        serializer = serializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def _delete_method_actions(self, request, pk, model):
        user = request.user
        crypto = get_object_or_404(Cryptocurrency, id=pk)
        model_object = get_object_or_404(model, user=user, crypto=crypto)
        model_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    @action(detail=True, methods=["POST"],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        return self._post_method_actions(
            request=request, pk=pk, serializers=FavoriteSerializer
        )

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        return self._delete_method_actions(
            request=request, pk=pk, model=Favorite
        )

    @action(detail=True, methods=['GET'], url_path='news')
    def news(self, request, pk=None):
        # Получить объект криптовалюты
        crypto = self.get_object()

        # Запросить новости с использованием API
        # (в этом примере, используется NewsAPI)
        api_key = settings.NEWS_API_KEY
        url = f'https://newsapi.org/v2/everything?q={crypto.name}'\
              f'&apiKey={api_key}'
        response = requests.get(url)

        # Обработать ответ
        data = response.json()
        if response.status_code == 200:
            # Если запрос прошел успешно, создать список объектов новостей
            articles = data['articles']

            # Проверить наличие поля url_to_image в каждой новости
            for article in articles:
                if 'urlToImage' not in article:
                    article['urlToImage'] = None

            serializer = NewsSerializer(articles, many=True)
            return Response(serializer.data)
        else:
            # Если запрос не удался, вернуть код ошибки и сообщение
            return JsonResponse({'error': data['message']},
                                status=response.status_code)
