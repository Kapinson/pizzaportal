from django.shortcuts import render
from .models import Appetizer
# Create your views here.

def appetizer_list(request):
    all_appetizers = Appetizer.objects.all()

    response = render(request, "appetizers/appetizer_list.html", {'all_appetizers' : all_appetizers})
    return response