from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sandwich_list, name='sandwich_list'),
]
