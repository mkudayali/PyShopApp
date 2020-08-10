from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.newpage),
    path('detail/<int:proid>', views.detail)
]