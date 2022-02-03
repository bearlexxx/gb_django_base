from django.shortcuts import render
from productsapp.models import Product



def index (request):
    title = 'Магазин'

    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]

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

