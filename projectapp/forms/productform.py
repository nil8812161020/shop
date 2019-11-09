from django import forms
from projectapp.models import Product

#product form

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = {'name','price','description','discount','price_discount','stock','image'}
