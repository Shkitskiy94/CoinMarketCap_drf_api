from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CryptocurrencyViewSet, get

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('crypto', CryptocurrencyViewSet, basename='crypto')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('update_crypto/', get, name='update_crypto'),
]
