from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from orders.models import Order, OrderLine
from cart.cart import Cart

# Create your views here.

@login_required(login_url="/authentication/log_in")

def process_order(request):
    order=Order.objects.create(user=request.user)
    cart=Cart(request)
    orders_lines=list()
    for key, value in cart.cart.items():
        orders_lines.append(OrderLine(
            product_id=key,
            amount=value['amount'],
            user=request.user,
            order=order
        ))

    OrderLine.objects.bulk_create(orders_lines)

    sendMail(
        order=order,
        orders_lines=orders_lines,
        username=request.user.username,
        user_mail=request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../shop")

def sendMail(**kwargs):
    subject="Gracias por el pedido"
    message=render_to_string("emails/order.html", {
        "order": kwargs.get("orders"),
        "orders_lines": kwargs.get("orders_lines"),
        "username": kwargs.get("username")
    })

    text_message = strip_tags(message)
    from_email = "your-mail@gmail.com"
    to = kwargs.get("user_mail")

    send_mail(subject, text_message, from_email, [to], html_message=message)
