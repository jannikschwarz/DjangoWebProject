# Generated by Django 2.2.28 on 2022-05-04 20:35

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220504_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='default_price',
            new_name='price',
        ),
        migrations.AddField(
            model_name='drink',
            name='size',
            field=models.CharField(choices=[('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE')], default=app.models.Size('S'), max_length=1),
        ),
    ]