from django.urls import path
from .views import * 

urlpatterns = [
    path('customeradd/', CustomerAdd, name='addcustomer'),
    path('customerall/', AllCustomer, name='allcustomer'),
    path('customerdelete/<int:id>/', DeleteCustomer, name='deletecustomer'),
    path('customerupdate/<int:id>/', UpdateCustomer, name='updatecustomer'),

    path('add/orders',OrederAdd, name='addorders'),
    path('orders/', OrdersList, name='orders'),
    path('delete/order/<int:id>/', OrdersDelete, name='deleteorder'),
    path('update/order/<int:id>', OrderUpdate, name='updateorder'),
]
