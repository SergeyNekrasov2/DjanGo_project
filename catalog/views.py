from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def index(request):
    return render(request, "base.html")

# def create(request):
#     if request.method == "POST":
#         product = Product()
#         product.name = request.POST.get("product")
#         product.descriptions = request.POST.get("descriptions")
#         product.category = request.POST.get("category")
#         product.price = request.POST.get("price")
#         product.save()
#     return HttpResponseRedirect("/")
