"""
Definition of forms.
"""

from django import forms
from .models import Order
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class OrderForm(forms.ModelForm):
    customer = forms.CharField(label=_("Customer name"),
                              widget=forms.TextInput({
                                  'class': 'form-control'}))
    class Meta:
        model = Order
        exclude = ['products', 'order_created', 'price']
