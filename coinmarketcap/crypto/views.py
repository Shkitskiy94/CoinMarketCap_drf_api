from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.db.models import Q

from api.models import Cryptocurrency, Favorite
from .forms import CryptoForm, CryptoUpdateForm


class Home(ListView):
    model = Cryptocurrency
    template_name = 'crypto/index.html'
    context_object_name = 'crypto_home'
    paginate_by = 100


class SearchHome(ListView):
    model = Cryptocurrency
    template_name = 'crypto/search.html'
    context_object_name = 'crypto_home'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            search_list = Cryptocurrency.objects.filter(
                Q(name__icontains=query) | Q(symbol__icontains=query)
            )
        else:
            search_list = Cryptocurrency.objects.none()
        return search_list


class CryptoHome(DetailView):
    model = Cryptocurrency
    template_name = 'crypto/crypto.html'
    context_object_name = 'crypto'
    slug_url_kwarg = 'symbol'
    allow_empty = True

    def get_object(self, queryset=None):
        crypto_symbols = self.kwargs['crypto_symbols']
        return get_object_or_404(Cryptocurrency, symbol=crypto_symbols)



@login_required
def favorites(request):
    favorite_cryptos = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html',
                  {'favorite_cryptos': favorite_cryptos})


@login_required
def add_favorite(request):
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            crypto_id = form.cleaned_data['crypto_id']
            crypto = Cryptocurrency.objects.get(id=crypto_id)
            Favorite.objects.create(user=request.user, crypto=crypto)
            messages.success(request, f'{crypto.name} добавлена в избранное')
            return redirect('favorites')
    else:
        form = CryptoForm()
    return render(request, 'add_favorite.html', {'form': form})


@login_required
def update_crypto(request, crypto_id):
    crypto = get_object_or_404(Cryptocurrency, id=crypto_id)
    if request.method == 'POST':
        form = CryptoUpdateForm(request.POST, instance=crypto)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Криптовалюта {crypto.name} успешно обновлена')
            return redirect('home')
    else:
        form = CryptoUpdateForm(instance=crypto)
    return render(request, 'update_crypto.html', {'form': form})
