# from lib2to3.fixes.fix_input import context
# from gc import get_object

from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponseNotFound

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


# def index(request):
#     return render(request, "base.html")

def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {'product': product}
    return render(request, 'products_list.html', context)
