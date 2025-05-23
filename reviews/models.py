from django.db import models
from django.conf import settings
# Create your models here.


class Review(models.Model):
    """"
    This class defines the reviews that users can leave for products.
    It has a foreign key to the product and user who left the review.
    """
    product = models.ForeignKey(
        'store.Product',
        on_delete=models.CASCADE,
        related_name="reviews"
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        verification_status = 'Verified' if self.verified else 'Unverified'
        return (
            f"{self.user.username} - {self.product.name} "
            f"({verification_status})"
        )
