from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from .models import Item, Cart

def capture_signs(request):
    # Your sign capturing logic here
    return render(request, 'capture_signs.html')

def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    cart = Cart.objects.create(item=item)
    # Additional logic for adding items to the cart
    return render(request, 'cart.html', {'cart': cart})
