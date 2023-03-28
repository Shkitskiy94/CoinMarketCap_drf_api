from django.urls import path
from .views import Home, SearchHome, CryptoHome
from . import views

app_name = 'crypto'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', SearchHome.as_view(), name='search'),
    path('crypto/<slug:crypto_symbols>/', CryptoHome.as_view(),
         name='crypto_detail'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('update_crypto/<int:crypto_id>/',
         views.update_crypto, name='update_crypto'),
]
