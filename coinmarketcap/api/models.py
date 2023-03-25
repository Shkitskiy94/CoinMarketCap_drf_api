from django.db import models

class Cryptocurrency(models.Model):
    identifier = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    change_24h = models.DecimalField(max_digits=5, decimal_places=2)
    volume_24h = models.DecimalField(max_digits=20, decimal_places=2)
