"""
Definition of models.
"""

from django.db import models
from enum import Enum

class Product(models.Model): 
    name = models.CharField(
        max_length = 100)
    price = models.DecimalField(
        max_digits= 6,
        decimal_places= 2)
    def init(name, price):
        this.name = name
        this.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

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
    size = models.CharField(
        max_length = 1,
        choices = [(tag.value, tag.name) for tag in Size] 
        )
    def init(name, price , size):
        this.name = name
        this.price = price
        this.size = size
         
    def getSize(self):
        return self.size

    def getPrice(self):
        if(self._Drinksize == Size.SMALL): return price + 0
        elif(self._Drinksize == Size.MEDIUM) : return price + 5
        elif(self._Drinksize == Size.LARGE) : return price + 10

class Soda(Drink):
    price = 7
    sodaType = 'Soda'
    def init(name, size, sodaType):
        this.name = name
        this.size = size
        this.sodaType = sodaType

class Juice(Drink):
    price = 5
    juiceType = 'Juice'
    def init(name, size, juiceType):
        this.name = name
        this.size = size
        this.juiceType = juiceType

class Coffee(Drink):
    price = 10
    coffeeType = 'Coffee'
    def init(name, size, coffeeType):
        this.name = name
        this.size = size
        this.coffeeType = coffeeType



# Create your models here.
