from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    avatar = models.ImageField(upload_to='profile/avatars/', null=True, blank=True)
    banner = models.ImageField(upload_to='profile/banners/', null=True, blank=True)
    description = models.TextField(blank=True, null=True, default='')

    phone = models.CharField(
        max_length=11,
        blank=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
