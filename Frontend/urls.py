from django.urls import path
from Inventory.views import * 

urlpatterns = [
    path('', index, name='home'),
]