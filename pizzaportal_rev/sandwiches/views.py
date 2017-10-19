from django.shortcuts import render
from .models import Sandwich
# Create your views here.

def sandwich_list(request):
    all_sandwiches = Sandwich.objects.all()

    response = render(request, 'sandwiches/sandwich_list.html', {'all_sandwiches' : all_sandwiches})
    return response