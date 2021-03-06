# Generated by Django 2.2.28 on 2022-05-04 17:42

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('default_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Product')),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE')], default=app.models.Size('S'), max_length=1)),
                ('type', models.CharField(max_length=100, null=True)),
            ],
            bases=('app.product',),
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('drink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Drink')),
            ],
            bases=('app.drink',),
        ),
        migrations.CreateModel(
            name='Juice',
            fields=[
                ('drink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Drink')),
            ],
            bases=('app.drink',),
        ),
        migrations.CreateModel(
            name='Soda',
            fields=[
                ('drink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Drink')),
            ],
            bases=('app.drink',),
        ),
    ]
