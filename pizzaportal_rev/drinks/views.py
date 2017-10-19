from django.shortcuts import render
from .models import Drink
# Create your views here.

def drink_list(request):
    all_drinks = Drink.objects.all()

    response = render(request, "drinks/drink_list.html", {'all_drinks' : all_drinks})
    return response