from django.urls import path

from .views import (
    ProductListView,
    AboutView,
    ProductDetailView,
    CategoryListView,
    category,
    like_product,
    delete_like_product,
    add_review,
    edit_review,
    delete_review,
)


urlpatterns = [
    # Home
    path('', ProductListView.as_view(), name='home'),

    # About
    path('about/', AboutView.as_view(), name='about'),

    # Product details
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),

    # Categories
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', category, name='category'),

    # Like / Unlike
    path('like/<int:pk>/', like_product, name='like_product'),
    path('delete-like/<int:pk>/', delete_like_product, name='delete_like'),

    # Reviews
    path('product/<int:pk>/review/', add_review, name='add_review'),
    path('review/<int:pk>/edit/', edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', delete_review, name='delete_review'),
]