from django.contrib import admin
from .models import Product
from .models import Drink
from .models import Soda
from .models import Coffee
from .models import Juice

admin.site.register(Product)
admin.site.register(Drink)
admin.site.register(Soda)
admin.site.register(Coffee)
admin.site.register(Juice)