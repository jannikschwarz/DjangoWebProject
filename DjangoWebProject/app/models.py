"""
Definition of models.
"""

from django.db import models
from enum import Enum

class Product(models.Model): 
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits= 6,
        decimal_places= 2,
        default = 10)

class Size(Enum):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

class JuiceType(Enum):
    AppleJuice = 'Apple'
    OrangeJuice = 'Orange'
    MultiJuice = 'Multi'

class SodaType(Enum):
    Fanta = 'Fanta'
    Cola = 'Cola'
    Sprite = 'Sprite'

class CoffeeType(Enum):
    Americano = 'Americano'
    Cappuccino = 'Cappuccino'
    CaffeeLatte = 'Caffee Latte'

class Drink(Product):
    size = models.CharField(max_length = 1,
        choices = [(tag.value, tag.name) for tag in Size],
        default = Size.SMALL)

class Soda(Drink):
    subtype = models.CharField(max_length = 100,
        choices = [(tag.value, tag.name) for tag in SodaType],
        default = SodaType.Cola)
    price = 7

class Juice(Drink):
    subtype = models.CharField(max_length = 100,
        choices = [(tag.value, tag.name) for tag in JuiceType],
        default = JuiceType.AppleJuice)
    price = 7

class Coffee(Drink):
    subtype = models.CharField(max_length = 100,
        choices = [(tag.value, tag.name) for tag in CoffeeType],
        default = CoffeeType.Americano)
    price = 10

class Order(models.Model):
    products = models.ManyToManyField(Product, blank = True)
    customer = models.CharField(max_length = 100,
        null = True)
    order_created = models.DateTimeField(auto_now_add = True)


# Create your models here.
