from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart(request, tot=0, count=0, ct_items=None):
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += i.product.price * i.quantity
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
        return ct_id


def cart_add(request, product_id):
    prod = Prod.objects.get(id=product_id)
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
    except ObjectDoesNotExist:
        ct = Cartlist.objects.create(cart_id=c_id(request))
        ct.save()
        # return redirect('cart')
    try:
        c_items = Items.objects.get(product=prod, cart=ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity += 1
            c_items.save()
            # return redirect('cart')

    except ObjectDoesNotExist:
        c_items = Items.objects.create(product=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cart')


def min_cart(request, product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(Prod, id=product_id)
    c_items = Items.objects.get(product=prodt, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
        # return redirect('cart')
    else:
        c_items.delete()
    return redirect('cart')


def del_cart(request, product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(Prod, id=product_id)
    c_items = Items.objects.get(product=prodt, cart=ct)
    c_items.delete()
    return redirect('cart')

