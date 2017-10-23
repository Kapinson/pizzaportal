from django.shortcuts import render
from .models import Drink
from pizzaportal.views import *
# Create your views here.

def drink_list(request):
    template_path = 'drinks/drink_list.html'
    all_drinks = consumable_list(request, Drink, 'drinks')

    if(all_drinks != None):  
        response = render(request, template_path, {'all_drinks' : all_drinks,})                                                         
        return response
    else:
        print("Redirecting to Orders...")
        return redirect('order_list')