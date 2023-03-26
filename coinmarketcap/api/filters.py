from django_filters.rest_framework import FilterSet

from .models import Cryptocurrency


class CryptocurrencyFilter(FilterSet):
    class Meta:
        model = Cryptocurrency
        fields = ('name', 'symbol')
