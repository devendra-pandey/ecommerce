from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'order/cart.html')

def checkout(request):
    return render(request, 'order/checkout.html')

def invoice(request):
    return render(request, 'order/invoice.html')