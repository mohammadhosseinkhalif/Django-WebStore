from .cart import Cart

def cart_items(request):
    return {'cart': Cart(request)}