from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem


@login_required
def checkout(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    items = CartItem.objects.filter(cart=cart)

    total = 0

    for item in items:
        total += item.subtotal()

    context = {
        "items": items,
        "total": total,
    }

    return render(request, "orders/checkout.html", context)