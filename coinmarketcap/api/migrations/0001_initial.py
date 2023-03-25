# Generated by Django 4.1.7 on 2023-03-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('identifier', models.IntegerField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('change_24h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('volume_24h', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
