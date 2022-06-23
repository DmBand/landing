from django.shortcuts import render
from .models import Product


def index_view(request):
    """ Главная страница """

    chockolate = Product.objects.filter(category=1).order_by('-date_added')
    marshmallow = Product.objects.filter(category=2).order_by('-date_added')
    marmalade = Product.objects.filter(category=3).order_by('-date_added')
    context = {
        'chockolate': chockolate,
        'marshmallow': marshmallow,
        'marmalade': marmalade
    }
    return render(request, 'landing_app/index.html', context)
