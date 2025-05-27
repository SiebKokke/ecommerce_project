from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Store(models.Model):
    """
    This class defines the store and store owner.
    Limits each store to one owner.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "vendor"},
        related_name="stores"
    )
    logo = models.ImageField(upload_to="store_logos/", blank=True, null=True)

    def __str__(self):
        """
        Makes name more readable.
        """
        return self.name


class Product(models.Model):
    """
    Defines the products that owners can put in the store.
    Also has inventory count so owners know how much inventory they have.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="products"
    )
    inventory_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to="product_images/", blank=True, null=True
    )

    def __str__(self):
        """
        Makes name an store name more readable.
        """
        return f"{self.name} ({self.store.name})"
