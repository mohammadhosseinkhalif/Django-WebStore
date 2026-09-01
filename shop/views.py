from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg
from django.views.generic import ListView, TemplateView, DetailView
from django.utils.decorators import method_decorator

from cart.cart import Cart
from shop.models import Product, Category, LikedItems, Review


# ----- Helpers -----

def update_product_score(product):
    """Recalculate product's average star rating and save it."""
    average_score = Review.objects.filter(product=product).aggregate(
        average=Avg('star')
    )['average']
    product.score = average_score or 0
    product.save(update_fields=['score'])


# ----- Class-Based Views -----

class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'


class AboutView(TemplateView):
    template_name = 'shop/about.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        # Product media
        context['media_list'] = product.media.all()

        # Cart status
        cart = Cart(self.request)
        context['in_cart'] = cart.chek_product(product)

        # Like status
        if self.request.user.is_authenticated:
            context['is_like'] = LikedItems.objects.filter(
                product=product, user=self.request.user
            ).exists()
        else:
            context['is_like'] = False

        # Reviews
        reviews = Review.objects.filter(product=product).select_related(
            'user', 'user__profile'
        ).order_by('-id')
        context['reviews'] = reviews

        # Current user's review
        if self.request.user.is_authenticated:
            context['user_review'] = reviews.filter(
                user=self.request.user
            ).first()
        else:
            context['user_review'] = None

        return context


# ----- Function-Based Views -----

def category(request, pk):
    cat = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=cat)

    if not products.exists():
        messages.info(request, 'کالایی در این دسته بندی موجود نیست.')
        return redirect('home')

    return render(request, 'shop/category.html', {
        'products': products,
        'cat': cat,
    })


@login_required
def like_product(request, pk):
    if request.method != 'POST':
        return redirect('home')

    product = get_object_or_404(Product, id=pk)
    LikedItems.objects.get_or_create(product=product, user=request.user)
    return JsonResponse({'like': True})


@login_required
def delete_like_product(request, pk):
    if request.method != 'POST':
        return redirect('home')

    product = get_object_or_404(Product, id=pk)
    LikedItems.objects.filter(product=product, user=request.user).delete()
    return JsonResponse({'delete_like': True})


@login_required
def add_review(request, pk):
    """Add a new review for the product (one per user)."""
    product = get_object_or_404(Product, id=pk)

    if request.method != 'POST':
        return redirect('product_details', pk=product.id)

    text = request.POST.get('comment', '').strip()
    star = request.POST.get('score')

    # Validate comment
    if not text:
        messages.error(request, 'لطفاً متن نظر خود را وارد کنید.')
        return redirect('product_details', pk=product.id)

    # Validate score
    try:
        star = int(star)
    except (TypeError, ValueError):
        messages.error(request, 'امتیاز وارد شده معتبر نیست.')
        return redirect('product_details', pk=product.id)

    if star < 1 or star > 5:
        messages.error(request, 'امتیاز باید بین ۱ تا ۵ باشد.')
        return redirect('product_details', pk=product.id)

    # Prevent duplicate review
    if Review.objects.filter(product=product, user=request.user).exists():
        messages.warning(request, 'شما قبلاً برای این محصول نظر ثبت کرده‌اید.')
        return redirect('product_details', pk=product.id)

    Review.objects.create(
        product=product,
        user=request.user,
        text=text,
        star=star
    )
    update_product_score(product)

    messages.success(request, 'نظر شما با موفقیت ثبت شد.')
    return redirect('product_details', pk=product.id)


@login_required
def delete_review(request, pk):
    """Delete the logged-in user's review."""
    review = get_object_or_404(Review, id=pk, user=request.user)
    product = review.product

    if request.method != 'POST':
        return redirect('product_details', pk=product.id)

    review.delete()
    update_product_score(product)

    messages.success(request, 'نظر شما با موفقیت حذف شد.')
    return redirect('product_details', pk=product.id)


@login_required
def edit_review(request, pk):
    """Edit the logged-in user's review."""
    review = get_object_or_404(Review, id=pk, user=request.user)
    product = review.product

    if request.method != 'POST':
        return redirect('product_details', pk=product.id)

    text = request.POST.get('comment', '').strip()
    star = request.POST.get('score')

    if not text:
        messages.error(request, 'لطفاً متن نظر خود را وارد کنید.')
        return redirect('product_details', pk=product.id)

    try:
        star = int(star)
    except (TypeError, ValueError):
        messages.error(request, 'امتیاز وارد شده معتبر نیست.')
        return redirect('product_details', pk=product.id)

    if star < 1 or star > 5:
        messages.error(request, 'امتیاز باید بین ۱ تا ۵ باشد.')
        return redirect('product_details', pk=product.id)

    review.text = text
    review.star = star
    review.save(update_fields=['text', 'star'])
    update_product_score(product)

    messages.success(request, 'نظر شما با موفقیت ویرایش شد.')
    return redirect('product_details', pk=product.id)


def custom_404(request, exception):
    return render(request, 'shop/404.html', status=404)