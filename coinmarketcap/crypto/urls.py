from django.urls import path
from .views import (Home, SearchHome, CryptoHome, CryptoCreateView,
                    CryptoUpdateView, CryptoDeleteView)


app_name = 'crypto'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', SearchHome.as_view(), name='search'),
    path('crypto/<slug:crypto_symbols>/', CryptoHome.as_view(),
         name='crypto_detail'),
    path('create/', CryptoCreateView.as_view(), name='create'),
    path('<str:symbol>/update/', CryptoUpdateView.as_view(), name='update'),
    path('<str:symbol>/delete/', CryptoDeleteView.as_view(), name='delete'),
#     path('create/', CryptoCreateView.as_view(), name='create'),
#     path('update/<slug:symbol>/', CryptoUpdateView.as_view(), name='update'),
#     path('<slug:symbol>/favorite/', FavoriteCreateView.as_view(),
#          name='favorite_create'),
#     path('<int:pk>/favorite/delete/', FavoriteDeleteView.as_view(),
#          name='favorite_delete'),
]
