from django.shortcuts import render, redirect, HttpResponse
from django.template.defaulttags import register
from decimal import *


from .forms import OrderForm

from .models import Order
from pizzas.models import Pizza

# Create your views here.

def order_list(request):
    pizzas = Pizza.objects.all()
    my_order = request.session.get('order')
    my_order = order_convert(my_order)
    total_price = total_order_price(my_order, pizzas)

    if request.method == "POST":

        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.consumables = total_order_consumeables(my_order, pizzas)
            order.total_price = total_price
            order.save()
            #return redirect('post_detail', pk=order.pk) wywala na post_detail nie używaj
            form = OrderForm()
            print('Zamówienie zatwierdzone i zapisane w bazie')
    else:
        form = OrderForm()

    response = render(request, 'orders/order_list.html', {'pizzas' : pizzas,
                                                          'my_order' : my_order,
                                                          'form':form,
                                                          'total_price':total_price})
    return response

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def consumeable_quantity_to_price(quantity, price):
    return(int(quantity)*int(price))

def total_order_price(my_order, pizzas):
    total_price = 0
    for prop in my_order:
        for pizza in pizzas:
            if pizza.id == prop:
                total_price += consumeable_quantity_to_price(get_item(my_order, prop), pizza.price)
    return(Decimal(total_price))

def total_order_consumeables(my_order, pizzas):
    total_consumeables = ''
    for prop in my_order:
        for pizza in pizzas:
            if pizza.id == prop:
                total_consumeables += pizza.name + ', '
    return(total_consumeables)

def order_convert(my_order):
    if my_order != '':
        my_order = my_order.split(',')
        my_order = {int(i):my_order.count(i) for i in my_order}
        return (my_order)


