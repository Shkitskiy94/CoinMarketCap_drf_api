from django.contrib import admin

from .models import Cryptocurrency, Favorite


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name',
                    'price', 'change_24h', 'volume_24h')
    search_fields = ('symbol', 'name')
    list_filter = ('symbol', 'name')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'crypto')
    search_fields = ('user', 'crypto')
    list_filter = ('user', 'crypto')