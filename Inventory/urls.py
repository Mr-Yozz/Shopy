from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.index, name='home'),
    # path('products/', views.AllProducts, name='allProducts'),
    # path('product/add', views.ProductsAdd, name='Product_add'),
    # path('product/delete/<int:id>/', views.DeleteProducts, name='deleteProduct'),
    # path('product/update/<int:id>/', views.ProductUpdate, name='UpdateProduct'),

    path('products/add/', views.ProductsAddView.as_view(), name = 'Product_add'),
    path('products/', views.ProductsListView.as_view(), name='allProducts'),
    path('product/delete/<int:id>/', views.ProductDeleteView.as_view(), name='deleteProduct'),
    path('product/update/<int:id>/', views.ProductUpdateView.as_view(), name='UpdateProduct'),






]   


