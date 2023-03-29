from django.urls import path

from .views import (AddFavoriteView, CryptoCreateView, CryptoDeleteView,
                    CryptoHome, CryptoUpdateView, FavoriteListView, Home,
                    RemoveFavoriteView, SearchHome)

app_name = 'crypto'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', SearchHome.as_view(), name='search'),
    path('crypto/<slug:crypto_symbols>/', CryptoHome.as_view(),
         name='crypto_detail'),
    path('create/', CryptoCreateView.as_view(), name='create'),
    path('<int:id>/update/', CryptoUpdateView.as_view(), name='update'),
    path('<str:symbol>/delete/', CryptoDeleteView.as_view(), name='delete'),
    path('favorites/', FavoriteListView.as_view(), name='favorite_list'),
    path('favorites/add/<int:crypto_id>/', AddFavoriteView.as_view(),
         name='add_favorite'),
    path('favorites/remove/<int:crypto_id>/', RemoveFavoriteView.as_view(),
         name='remove_favorite'),
]
