from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cryptocurrency(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=38, decimal_places=8)
    change_24h = models.DecimalField(max_digits=38, decimal_places=8)
    volume_24h = models.DecimalField(max_digits=38, decimal_places=8)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='favorite',
        to=User,
        verbose_name='пользователь',
    )
    crypto = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='crypto',
        to=Cryptocurrency,
        verbose_name='криптовалюта',
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'crypto'),
                name='unique_favorite'
            )
        ]
        verbose_name = 'избранная криптовалюта'
        verbose_name_plural = 'избранные криптовалюты'

    def __str__(self):
        return f'{self.user} добавил {self.crypto} в список избранных'
