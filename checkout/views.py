from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NeKtYAwpLA9i7SBGTf0hyMiDsU3AEAa5RUspjksNbdOKel9Ff3X1DWXrx5nX4OrwbCBXVSk2MAJ1gXD67N0HyrZ00aOvCZNKi',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
