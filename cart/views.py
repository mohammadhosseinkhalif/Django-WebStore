from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from shop.models import Product
from .cart import Cart


class CartView(TemplateView):
    """Display the current shopping cart."""
    template_name = 'cart/cart_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['products'] = cart.get_products()
        return context


@require_POST
def cart_add(request):
    """Add a product to the cart via AJAX."""
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    cart_quantity = len(cart)  # uses __len__ implicitly
    messages.success(request, 'به سبد خرید اضافه شد')
    return JsonResponse({'cart_quantity': cart_quantity})


@require_POST
def cart_remove(request):
    """Remove a product from the cart via AJAX."""
    product_id = request.POST.get('product_id')
    cart = Cart(request)
    cart.remove(product_id)
    cart_quantity = len(cart)
    messages.success(request, 'از سبد خرید حذف شد')
    return JsonResponse({'cart_quantity': cart_quantity})