from django_filters.rest_framework import FilterSet, filters
from .models import Cryptocurrency
from rest_framework.filters import SearchFilter


class CryptocurrencySearchFilter(SearchFilter):
    search_param = ('name', 'symbol')



class CryptocurrencyFilter(FilterSet):
    class Meta:
        model = Cryptocurrency
        fields = ('name', 'symbol')