from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.shortcuts import render,redirect, get_object_or_404
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.conf import settings # new
from django.http.response import JsonResponse 


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    print(order)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})



def invoice(request):
    return render(request, 'order/invoice.html')


def order_create(request):
    user_id = request.user.id
    print("**** the user is is ")
    print(user_id)
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,'order/checkout.html',{'cart': cart, 'form': form})


