from django.http import HttpResponse
from django.shortcuts import render


def deploy(request):
    return render(request, 'deploy.html')

