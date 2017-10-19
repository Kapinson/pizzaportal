from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pizza_list, name='pizza_list'),
]
