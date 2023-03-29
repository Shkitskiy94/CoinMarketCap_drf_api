import requests
from api.models import Cryptocurrency, Favorite
from api.serializers import NewsSerializer
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CryptoForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crypto = self.get_object()
        api_key = settings.NEWS_API_KEY
        url = f'https://newsapi.org/v2/everything?q={crypto.name}'\
              f'&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            articles = data['articles']
            for article in articles:
                if 'urlToImage' not in article:
                    article['urlToImage'] = None
            serializer = NewsSerializer(articles, many=True)
            context['articles'] = serializer.data
        else:
            context['error'] = data['message']
        return context


class CryptoCreateView(CreateView):
    model = Cryptocurrency
    form_class = CryptoForm
    template_name = 'crypto/create.html'
    success_url = reverse_lazy('crypto:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CryptoUpdateView(UpdateView):
    model = Cryptocurrency
    form_class = CryptoForm
    template_name = 'crypto/update.html'
    slug_url_kwarg = 'simbol'
    success_url = reverse_lazy('crypto:home')

    def get_object(self, queryset=None):
        crypto_id = self.kwargs['id']
        return get_object_or_404(Cryptocurrency, id=crypto_id)

    def form_valid(self, form):
        form.instance.symbol = self.request.POST.get('symbol')
        form.instance.name = self.request.POST.get('name')
        form.instance.price = self.request.POST.get('price')
        form.instance.change_24h = self.request.POST.get('change_24h')
        form.instance.volume_24h = self.request.POST.get('volume_24h')
        self.object = form.save()
        return super().form_valid(form)


class CryptoDeleteView(DeleteView):
    model = Cryptocurrency
    template_name = 'crypto/delete.html'
    success_url = reverse_lazy('crypto:home')
    slug_url_kwarg = 'symbol'

    def get_object(self, queryset=None):
        crypto_symbol = self.kwargs['symbol']
        return get_object_or_404(Cryptocurrency, symbol=crypto_symbol)


class FavoriteListView(LoginRequiredMixin, View):
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        return render(request, 'crypto/favorites.html',
                      {'favorites': favorites})


class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, crypto_id):
        crypto = get_object_or_404(Cryptocurrency, id=crypto_id)
        if not Favorite.objects.filter(user=request.user,
                                       crypto=crypto).exists():
            Favorite.objects.create(user=request.user, crypto=crypto)
        return redirect('crypto:favorite_list')


class RemoveFavoriteView(LoginRequiredMixin, View):
    def post(self, request, crypto_id):
        crypto = Cryptocurrency.objects.get(id=crypto_id)
        Favorite.objects.filter(user=request.user, crypto=crypto).delete()
        return redirect('crypto:favorite_list')
