from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your function-base views here.

def index(request):

    context = {
        "name" : "Yozz",
        "Role":"admin",
        # "Role":"manager",
        # "Role":"Guset",
        "age":"23",
        "numbers":[1,2,3,4,5],
        "language":{
            "tamil":100,
            "english":99,
            }
    }
    return render(request, 'home.html',context)

def ProductsAdd(request):
    context = {
        'product_form':Product_Form()
    }
    if request.method == "POST":
        # print(request.POST)
        product_form = Product_Form(request.POST)
        if product_form.is_valid():

            product_form.save()
    return render(request, 'products_add.html', context)

def AllProducts(request):
    # all_products = Product.objects.all()
    context = {
        "all_products" : Product.objects.all()
    }
    return render(request, 'products.html',context)

def DeleteProducts(request, id):
    selected_product = Product.objects.get(id = id)
    selected_product.delete()
    return redirect('allProducts')

def ProductUpdate(request, id):
    selected_product = Product.objects.get(id = id)
    context = {
        'product_form' : Product_Form(instance = selected_product),
    }
    if request.method == 'POST':
        product_form = Product_Form(request.POST, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('allProducts')
    return render(request, 'products_add.html', context)

# Create your class-base views here.

class ProductsAddView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request):
        context = {
        'product_form':Product_Form()
        }
        return render(request, 'products_add.html', context)

    def post(self, request):
        product_form = Product_Form(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('allProducts') 


class ProductsListView(View):

    def get(self, request):
        context = {
        "all_products" : Product.objects.all()
    }
        return render(request, 'products.html',context)

class ProductDeleteView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request, id):
        selected_product = Product.objects.get(id = id)
        selected_product.delete()
        return redirect('allProducts')

class ProductUpdateView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request, id):
        selected_product = Product.objects.get(id = id)
        context = {
            'product_form' : Product_Form(instance = selected_product),
        }
        return render(request, 'products_add.html', context)


    def post(self, request, id):
        selected_product = Product.objects.get(id = id)
        if request.method == 'POST':
            product_form = Product_Form(request.POST, instance=selected_product)
            if product_form.is_valid():
                product_form.save()
                return redirect('allProducts')
        