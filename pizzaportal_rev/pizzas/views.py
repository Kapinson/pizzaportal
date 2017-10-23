from django.shortcuts import render, redirect
from django.template.defaulttags import register
from .models import Pizza
from pizzaportal.views import *

# Create your views here.
def pizza_list(request):
    template_path = 'pizzas/pizza_list.html'
    all_pizzas = consumable_list(request, Pizza, 'pizzas')
        
    if(all_pizzas != None):  
        response = render(request, template_path, {'all_pizzas' : all_pizzas,})                                                         
        return response
    else:
        print("Redirecting to Orders...")
        return redirect('order_list')
        

    '''
    all_pizzas = Pizza.objects.all()
    my_pizza= ''
    if request.POST:
        my_pizza = request.COOKIES.get('pizzas')
        print(my_pizza)
        request.session['pizzas'] = my_pizza
        print(order_convert(request.session.get('pizzas')))
        return redirect('order_list')
        
    response = render(request, 'pizzas/pizza_list.html', {'all_pizzas' : all_pizzas, 'my_pizza': my_pizza})
    return response
    '''

'''

@register.filter
def order_convert(my_order):
    if my_order != '':
        my_order = my_order.split(',')
        my_order = {int(i):my_order.count(i) for i in my_order}
        return (my_order)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

'''