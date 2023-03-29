from api.models import Cryptocurrency
from django import forms


class CryptoForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ('name', 'symbol', 'price', 'change_24h', 'volume_24h')
