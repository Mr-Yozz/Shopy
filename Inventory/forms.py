from django import forms
from .models import *

class Product_Form(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    # class Meta:
    #     model = Product
    #     fields = ['product_name', 'price']

    widgets = {
        "product_name" : forms.TextInput(attrs={'id' : "form-control"}),
        "product_code" : forms.TextInput(attrs={'class' : "form-control"}),
        "price" : forms.NumberInput(attrs={'class' : "form-control"}),
        "gst" : forms.NumberInput(attrs={'class' : "form-control"}),
    }