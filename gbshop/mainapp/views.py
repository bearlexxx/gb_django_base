from django.shortcuts import render

def index (request):
    title = 'Магазин'
    context = {
        'title': title
    }
    return render(request, 'mainapp/index.html', context)

def contact (request):
    title = 'Контакты'
    context = {
        'title': title
    }
    return render(request, 'mainapp/contact.html', context)