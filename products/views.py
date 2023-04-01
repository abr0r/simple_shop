from django.shortcuts import render

from products.models import Product, Category

# Create your views here.



def index(request):
    context = {
        'title': 'Angren Shop',
        }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Katalog',
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)