from django.urls import path
from productsapp.views import products, product

app_name = 'productsapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('product/<int:pk>/', product, name='detail'),
]