from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.order_list, name='order_list'),
    url(r'^$', views.order_confirmed, name = 'order_confirmed'),
]
