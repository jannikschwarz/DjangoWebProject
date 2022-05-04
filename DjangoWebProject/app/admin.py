from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Drink)
admin.site.register(Soda)
admin.site.register(Coffee)
admin.site.register(Juice)
admin.site.register(Order)