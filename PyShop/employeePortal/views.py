from django.http import HttpResponse
from django.shortcuts import render


def deploy22(request):
    return render(request, 'deploy22.html')


def dd(request):
    return render(request, 'dd.html')