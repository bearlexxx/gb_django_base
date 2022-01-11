from django.shortcuts import render
from productsapp.models import Product

from basketapp.models import Basket


def index (request):
    title = 'Магазин'

    products = Product.objects.all() [:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)

def contact (request):
    title = 'Контакты'
    context = {
        'title': title
    }
    return render(request, 'mainapp/contact.html', context)