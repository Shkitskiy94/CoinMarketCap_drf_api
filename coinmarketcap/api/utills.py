from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def crypto_api():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '372f37f2-3165-4b75-87b7-d47ee44d5f1a',
    }

    session = Session()
    session.headers.update(headers)

    data_dict = {}
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for currency in data['data']:
            identifier = currency['id']
            symbol = currency['symbol']
            name = currency['name']
            price = currency['quote']['USD']['price']
            change_24h = currency['quote']['USD']['percent_change_24h']
            volume_24h = currency['quote']['USD']['volume_24h']
            data_dict[symbol] = {'identifier': identifier, 'name': name,
                                'price': price, 'change_24h': change_24h,
                                'volume_24h': volume_24h}
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    with open('cryptocurrencies.json', 'w') as fp:
        json.dump(data_dict, fp)

crypto_api()
# with open('cryptocurrencies.json') as f:
#     data = json.load(f)

# for symbol, values in data.items():
#     crypto = Cryptocurrency(
#         id=values['id'],
#         symbol=symbol,
#         name=values['name'],
#         price=values['price'],
#         change_24h=values['change_24h'],
#         volume_24h=values['volume_24h']
#     )
#     crypto.save()
