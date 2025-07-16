from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def CustomerAdd(request):
    context = {
        'customer_form':Customer_Form()
    }
    if request.method == "POST":
        # print(request.POST)
        customer_form = Customer_Form(request.POST)
        if customer_form.is_valid():

            customer_form.save()
    return render(request, 'customer_add.html', context)

@login_required(login_url='/')
def AllCustomer(request):
    # all_products = Product.objects.all()
    context = {
        "all_customer" : Customer.objects.all()
    }
    return render(request, 'customer.html',context)

@login_required(login_url='/')
def DeleteCustomer(request, id):
    selected_customer = Customer.objects.get(id = id)
    selected_customer.delete()
    return redirect('allcustomer')

@login_required(login_url='/')
def UpdateCustomer(request, id):
    selected_customer = Customer.objects.get(id = id)
    context = {
        'customer_form' : Customer_Form(instance = selected_customer),
    }
    if request.method == 'POST':
        customer_form = Customer_Form(request.POST, instance=selected_customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('allcustomer')
    return render(request, 'customer_add.html', context)


# Orders 
@login_required(login_url='/')
def OrederAdd(request):
    context = {
        'order_form':Order_Form()
    }
    if request.method == 'POST':
        seleted_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(seleted_product.price) * float(request.POST['quantity'])
        gst_amount = (amount * seleted_product.gst) / 100
        bill_amount = amount + gst_amount
        new_order = Orders(customer_reference_id = request.POST['customer_reference'], 
                           product_reference_id = request.POST['product_reference'], 
                           order_number = request.POST['order_number'],
                           order_date = request.POST['order_date'], 
                           quantity = request.POST['quantity'], 
                           amount = amount, 
                           gst_amount = gst_amount, 
                           bill_amount = bill_amount)
        new_order.save()
        return redirect('orders')
    return render(request, 'order_add.html', context)

@login_required(login_url='/')
def OrdersList(request):
    context = {
        'all_orders' : Orders.objects.all()
    }
    return render(request, 'orders.html', context)

@login_required(login_url='/')
def OrdersDelete(request, id):
    order = Orders.objects.get(id = id)
    order.delete()
    return redirect('orders')

@login_required(login_url='/')
def OrderUpdate(request, id):
    order = Orders.objects.get(id = id)
    context = {
        'order_form':Order_Form(instance=order)
    }
    if request.method == 'POST':
        seleted_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(seleted_product.price) * float(request.POST['quantity'])
        gst_amount = (amount * seleted_product.gst) / 100
        bill_amount = amount + gst_amount
        order_filter = Orders.objects.filter(id = id)
        order_filter.update(customer_reference_id = request.POST['customer_reference'], 
                           product_reference_id = request.POST['product_reference'], 
                           order_number = request.POST['order_number'],
                           order_date = request.POST['order_date'], 
                           quantity = request.POST['quantity'], 
                           amount = amount, 
                           gst_amount = gst_amount, 
                           bill_amount = bill_amount)
        return redirect('orders')
    return render(request, 'order_add.html', context)
