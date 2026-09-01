from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, default=None)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands/', null=True, default=None)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    pictures = models.FileField(upload_to='products/', null=True, default=None)
    price = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True, default=None)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.IntegerField()
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                blank=True, null=True)
    sell = models.IntegerField(default=0, blank=True, null=True)
    discounted = models.BooleanField(default=False, blank=True, null=True)
    discounted_price = models.DecimalField(max_digits=12, decimal_places=0, default=0, blank=True, null=True)
    def __str__(self):
        return self.name


class ProductMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'تصویر'),
        ('video', 'ویدیو'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='products/media/%Y/%m/%d/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'uploaded_at']

    def __str__(self):
        return f"{self.get_media_type_display()} - {self.product.name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product.name




class LikedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="likes"
    )



class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    text = models.TextField()

    star = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'user'],
                name='unique_product_review_per_user'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.product} - {self.star}'
