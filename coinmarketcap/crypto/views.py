from api.models import Cryptocurrency, Favorite
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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
    form_class = CryptoUpdateForm
    template_name = 'crypto/update.html'
    slug_url_kwarg = 'symbol'
    success_url = reverse_lazy('crypto:home')

    def get_object(self, queryset=None):
        crypto_symbol = self.kwargs['symbol']
        return get_object_or_404(Cryptocurrency, symbol=crypto_symbol)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CryptoDeleteView(DeleteView):
    model = Cryptocurrency
    template_name = 'crypto/delete.html'
    success_url = reverse_lazy('crypto:home')
    slug_url_kwarg = 'symbol'

    def get_object(self, queryset=None):
        crypto_symbol = self.kwargs['symbol']
        return get_object_or_404(Cryptocurrency, symbol=crypto_symbol)

# class FavoriteCreateView(CreateView):
#     model = Favorite
#     fields = []

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.crypto = (Cryptocurrency.objects.
#                                 get(symbol=self.kwargs['symbol']))
#         messages.success(self.request,
#                          f'{form.instance.crypto} была добавлена в избранное!')
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('crypto', kwargs={'symbol': self.kwargs['symbol']})


# class FavoriteDeleteView(DeleteView):
#     model = Favorite

#     def delete(self, request, *args, **kwargs):
#         messages.success(request,
#                          'Криптовалюта была удалена из списка избранных')
#         return super().delete(request, *args, **kwargs)

#     def get_success_url(self):
#         return reverse_lazy('crypto', kwargs={'symbol': self.kwargs['symbol']})
