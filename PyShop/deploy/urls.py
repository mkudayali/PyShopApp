from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('deploy/', views.deploy),
]
