from django.shortcuts import render, redirect
from django.template.defaulttags import register

"""
GLOBAL VIEWS METHODS FOR CONSUMABLE MODULES

consumable_list:
all_consumeables - wanted model
template_path - for example 'pizzas/pizza_list.html'
cookie_name - 'pizzas', 'sandwiches' etc.
"""
def consumable_list(request, all_consumables, cookie_name):
    all_consumables = all_consumables.objects.all()
    template_consumable_cookie= ''
    if request.POST:
        template_consumable_cookie = request.COOKIES.get(cookie_name)
        print(template_consumable_cookie)
        request.session[cookie_name] = template_consumable_cookie
        print(order_convert(request.session.get(cookie_name)))
        return (None)
    
    return(all_consumables)

@register.filter
def order_convert(my_order):
    if my_order != '':
        my_order = my_order.split(',')
        my_order = {int(i):my_order.count(i) for i in my_order}
        return (my_order)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)