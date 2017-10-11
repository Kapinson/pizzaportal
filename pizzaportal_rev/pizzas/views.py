from django.shortcuts import render, redirect
from django.template.defaulttags import register
from .models import Pizza
from orders.views import order_list

# Create your views here.
def pizza_list(request):
    all_pizzas = Pizza.objects.all()
    my_pizza= ''
    if request.POST:
        my_pizza = request.COOKIES.get('orderlist')
        print(my_pizza)
        request.session['order'] = my_pizza
        print(order_convert(request.session.get('order')))
        return redirect('order_list')
        
    response = render(request, 'pizzas/home.html', {'all_pizzas' : all_pizzas, 'my_pizza': my_pizza})
    return response

@register.filter
def order_convert(my_order):
    if my_order != '':
        my_order = my_order.split(',')
        my_order = {int(i):my_order.count(i) for i in my_order}
        return (my_order)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)