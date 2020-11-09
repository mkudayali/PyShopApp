from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.newpage),
    #path('detail/<int:proid>', views.detail),
    #path('productall/', views.productall),
    path('home/', views.getAllProducts),
    path('home/detail/<int:proid>', views.detail),
    path('dd/', views.dd),


]

#url(r'^admin/deploy/$', TemplateView.as_view(template_name='admin/index.html')),
#url(r'^admin/', include('django.contrib.admin.urls')),