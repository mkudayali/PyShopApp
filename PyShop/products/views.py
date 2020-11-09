from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, ProductMain, SampleMultipleImgProduct, ProductMainImgs

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

#return HttpResponse('Hello World')

def dd(request):
    return render(request, 'dd.html')

def newpage(request):
    return HttpResponse('This is New Page')


def detail(request, proid):
    product = ProductMain.objects.get(id=proid)
    prodPics = ProductMainImgs.objects.filter(show_id=proid)
    context = {'product': product, 'prodPics': prodPics}
    return render(request, 'detail.html', context)
    #product = Product.objects.get(id=proid)
    #return render(request, 'detail.html', {'product': product})


def getAllProducts(request):
    products = ProductMain.objects.all()
    prodPics = ProductMainImgs.objects.order_by('id').all()
    context = {'products': products, 'prodPics': prodPics}
    return render(request, 'home.html', context)