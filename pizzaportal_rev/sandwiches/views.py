from django.shortcuts import render
from .models import Sandwich
from pizzaportal.views import *
# Create your views here.

def sandwich_list(request):
    template_path = 'sandwiches/sandwich_list.html'
    all_sandwiches = consumable_list(request, Sandwich, 'sandwiches')

    if(all_sandwiches != None):  
        response = render(request, template_path, {'all_sandwiches' : all_sandwiches,})                                                         
        return response
    else:
        print("Redirecting to Orders...")
        return redirect('order_list')