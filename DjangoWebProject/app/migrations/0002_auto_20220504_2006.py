# Generated by Django 2.2.28 on 2022-05-04 18:06

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='size',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='type',
        ),
        migrations.AddField(
            model_name='coffee',
            name='subtype',
            field=models.CharField(choices=[('Americano', 'Americano'), ('Cappuccino', 'Cappuccino'), ('Caffee Latte', 'CaffeeLatte')], default=app.models.CoffeeType('Americano'), max_length=100),
        ),
        migrations.AddField(
            model_name='juice',
            name='subtype',
            field=models.CharField(choices=[('Apple', 'AppleJuice'), ('Orange', 'OrangeJuice'), ('Multi', 'MultiJuice')], default=app.models.JuiceType('Apple'), max_length=100),
        ),
        migrations.AddField(
            model_name='soda',
            name='subtype',
            field=models.CharField(choices=[('Fanta', 'Fanta'), ('Cola', 'Cola'), ('Sprite', 'Sprite')], default=app.models.SodaType('Cola'), max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6),
        ),
    ]
