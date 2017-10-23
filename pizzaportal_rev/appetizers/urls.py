from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.appetizer_list, name='appetizer_list'),
]
