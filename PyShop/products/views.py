from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

#return HttpResponse('Hello World')


def newpage(request):
    return HttpResponse('This is New Page')


def detail(request, proid):
    product = Product.objects.get(id=proid)
    return render(request, 'detail.html', {'product': product})