from django.conf.urls import url

from . import views


urlpatterns = [
    url('', views.UploadView.as_view()),
]
