from django.shortcuts import render, redirect

from .cart import Cart

from shop.models import Product


# Create your views here.

def add_product(request, product_id):

    cart=Cart(request)
    
    product=Product.objects.get(id=product_id)

    cart.add(product=product)

    return redirect("Tienda")

def delete_product(request, product_id):

    cart=Cart(request)
    
    product=Product.objects.get(id=product_id)

    cart.delete(product=product)

    return redirect("Tienda")

def reduce_product(request, product_id):

    cart=Cart(request)
    
    product=Product.objects.get(id=product_id)

    cart.reduce(product=product)

    return redirect("Tienda")

def clear_cart(request, product_id):

    cart=Cart(request)
    
    cart.clear_cart()

    return redirect("Tienda")