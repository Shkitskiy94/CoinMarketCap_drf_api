import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinmarketcap.settings')
django.setup()

import requests
from models import Cryptocurrency

def save_cryptocurrencies():
    response = requests.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
        params={'convert': 'USD'},
        headers={'Accepts': 'application/json',
                 'X-CMC_PRO_API_KEY': '372f37f2-3165-4b75-87b7-d47ee44d5f1a'})
    data = response.json()
    for currency in data['data']:
        identifier = currency['id']
        symbol = currency['symbol']
        name = currency['name']
        price = currency['quote']['USD']['price']
        change_24h = currency['quote']['USD']['percent_change_24h']
        volume_24h = currency['quote']['USD']['volume_24h']
        cryptocurrency = Cryptocurrency(identifier=identifier, symbol=symbol, name=name, price=price, change_24h=change_24h, volume_24h=volume_24h)
        cryptocurrency.save()

save_cryptocurrencies()