from django.urls import path
from productsapp.views import products, product
from django.views.decorators.cache import cache_page

app_name = 'productsapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('product/<int:pk>/', product, name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    # path('category/<int:pk>/page/<int:page>/', cache_page(3600)(products), name='page'),
]