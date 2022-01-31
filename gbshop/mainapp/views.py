from django.shortcuts import render
from productsapp.models import Product



def index (request):
    title = 'Магазин'

    products = Product.objects.all() [:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)

def contact (request):
    title = 'Контакты'
    context = {
        'title': title
    }
    return render(request, 'mainapp/contact.html', context)