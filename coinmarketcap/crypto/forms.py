from django import forms
from api.models import Cryptocurrency


class CryptoForm(forms.Form):
    crypto_id = forms.ModelChoiceField(queryset=Cryptocurrency.objects.all(),
                                       label='Выберите криптовалюту')


class CryptoUpdateForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'symbol', 'price', 'change_24h', 'volume_24h']
