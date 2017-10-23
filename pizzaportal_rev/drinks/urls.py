from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.drink_list, name='drink_list'),
]
