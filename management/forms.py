from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class SaleForm(forms.Form):
    quantity_sold = forms.IntegerField(min_value=1)