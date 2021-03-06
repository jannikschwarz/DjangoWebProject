"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import OrderForm
from .models import *

def create_order(request):
    """Renders the catalogue page."""
    assert isinstance(request, HttpRequest)
    context = {}
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        drinks = Drink.objects.all()
        context = { "drinks": drinks, "order": form.instance }
        return render(request, 'app/menu_drinks.html', context)

    context['form'] = form
    return render(
        request, 
        "app/create_order.html", 
        context)

def menu_drinks(request):
    assert isinstance(request, HttpRequest)
    if 'Checkout' in request.POST:
        order = Order.objects.get(pk=request.POST['order.id'])
        context = { "order": order }
        return render(request, "app/checkout.html", context)
    elif 'Add' in request.POST:
        drink = Product.objects.get(pk=request.POST['Add'])
        order = Order.objects.get(pk=request.POST['order.id'])
        order.addProduct(drink)
        drinks = Drink.objects.all()
        context = { "drinks": drinks, "order": order }
        return render(request, 'app/menu_drinks.html', context)
    else:
        return render(request, 'app/menu_drinks.html', {})


def checkout(request):
    order = Order.objects.get(pk=request.POST['order.id'])
    context = { "order": order }
    return render(request, "app/checkout.html", context)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def cafee(request):
    """Renders the cafee page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cafee.html',
        {
            'title':'Cafee',
            'message':'This is a simple cafee page' ,
            'year' : datetime.now().year,
        }
    )
