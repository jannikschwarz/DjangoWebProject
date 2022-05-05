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
    products = models.ManyToManyField(Product, blank = True, through = 'OrderProduct')
    customer = models.CharField(max_length = 100,
        null = True)
    order_created = models.DateTimeField(auto_now_add = True)
    price = models.DecimalField(null = True, 
        decimal_places = 2,
        max_digits = 7)

    def addProduct(self, prod):
        if prod in self.products.all():
            op = self.orderproduct_set.get(order = self, product = prod)
            op.count += 1
            op.save()
        else:
            self.products.add(prod)
        self.calcPrice()
        self.save()

    def calcPrice(self):
        self.price = 0
        for op in self.orderproduct_set.all():
            self.price += op.count * op.product.price

            
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    count = models.IntegerField(default = 1)


# Create your models here.
