"""
Definition of models.
"""

from django.db import models
from enum import Enum

class Product(models.Model): 
    name = models.CharField(
        max_length = 100)
    default_price = models.DecimalField(
        max_digits= 6,
        decimal_places= 2,
        default = 10)
    #def __init__():
    #    return
    #def __init__(name, price):
    #    this.name = name
    #    this.price = price

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
    size = Size.SMALL
    #size = models.CharField(
    #    max_length = 1,
    #    choices = [(tag.value, tag.name) for tag in Size],
    #    default = Size.SMALL
    #)
    #def __init__():
    #    return
    #def __init__(name, size):
    #    this.name = name
    #    this.size = size

    def setSize(self, size):
        self.size = size
         
    def getSize(self):
        return self.size

    def getPrice(self):
        if(self.size == Size.SMALL): return self.default_price
        elif(self.size == Size.MEDIUM) : return self.default_price + 5
        elif(self.size == Size.LARGE) : return self.default_price + 10

class Soda(Drink):
    subtype = models.CharField(
        max_length = 100,
        choices = [(tag.value, tag.name) for tag in SodaType],
        default = SodaType.Cola
    )
    default_price = 7
    #def __init__():
    #    return
    #def __init__(name, size, type):
    #    this.name = name
    #    this.size = size
    #    this.subtype = type

class Juice(Drink):
    subtype = models.CharField(
        max_length = 100,
        choices = [(tag.value, tag.name) for tag in JuiceType],
        default = JuiceType.AppleJuice
    )
    default_price = 5
    #def __init__():
    #    return
    #def __init__(name, size, type):
    #    this.name = name
    #    this.size = size
    #    this.subtype = type

class Coffee(Drink):
    subtype = models.CharField(
        max_length = 100,
        choices = [(tag.value, tag.name) for tag in CoffeeType],
        default = CoffeeType.Americano
    )
    default_price = 10
    #def __init__():
    #    return
    #def __init__(name, size, type):
    #    this.name = name
    #    this.size = size
    #    this.subtype = type



# Create your models here.
