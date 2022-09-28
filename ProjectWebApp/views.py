from django.shortcuts import render, HttpResponse
from cart.cart import Cart
from services.models import Service

# Create your views here.

def home(request):
    cart = Cart(request)
    
    return render(request, "ProjectWebApp/home.html")
