from django.shortcuts import render
from .models import Appetizer
from pizzaportal.views import *
# Create your views here.

def appetizer_list(request):
    template_path = "appetizers/appetizer_list.html"
    all_appetizers = consumable_list(request, Appetizer, 'appetizers')

    if(all_appetizers != None):  
        response = render(request, template_path, {'all_appetizers' : all_appetizers,})                                                         
        return response
    else:
        print("Redirecting to Orders...")
        return redirect('order_list')