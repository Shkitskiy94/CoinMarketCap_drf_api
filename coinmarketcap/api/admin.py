from django.contrib import admin

from .models import Cryptocurrency


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'symbol', 'name',
                    'price', 'change_24h', 'volume_24h')
    search_fields = ('symbol', 'name')
    list_filter = ('symbol', 'name')
