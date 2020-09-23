from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name= 'index'),
]