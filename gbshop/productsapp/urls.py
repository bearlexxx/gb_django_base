from django.urls import path
from productsapp.views import products

urlpatterns = [
    path('', products),
]