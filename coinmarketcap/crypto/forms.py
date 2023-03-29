from django import forms
from api.models import Cryptocurrency


class CryptoForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ('id', 'name', 'symbol', 'price', 'change_24h', 'volume_24h')


class CryptoUpdateForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'name', 'symbol', 'price', 'change_24h', 'volume_24h']
