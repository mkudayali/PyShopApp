from django.http import HttpResponse
from django.shortcuts import render
from .models import ImageUpload
from django.views.generic import ListView


class HomePageView(ListView):
    model = ImageUpload
    template_name = 'imageindex.html'


def index(request):
    imglist = ImageUpload.objects.all()
    return render(request, 'index.html',
                  {'imglist': imglist})


