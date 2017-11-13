from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.teste, name='teste'),
    url(r'^$', views.index, name='index'),
]