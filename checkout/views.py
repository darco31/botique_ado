from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L6gOzKBR501uaAx8yQW5xbTb6RaELPiw4l4vT9W49bChWPPnq4ZkSI9Ffpl7L536135ENV5JHj3ZkeZkUiEL40400ZdlN32Tv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)