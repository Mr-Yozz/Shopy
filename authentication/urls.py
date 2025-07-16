from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('signup/', SignupPage, name='signup'),
]
