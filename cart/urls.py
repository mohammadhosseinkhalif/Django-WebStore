from django.urls import path

from .views import CartView, cart_add, cart_remove

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', cart_add, name='add'),
    path('remove/', cart_remove, name='remove'),
]