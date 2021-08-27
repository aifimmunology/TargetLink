from django.urls import path
from django.conf.urls import url
from . import views

app_name='search'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^ajax/gene_details/$', views.gene_details, name='gene_details')
]