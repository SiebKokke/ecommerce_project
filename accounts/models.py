from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    """
    This class defines the role of the user in the system.
    Either a buyer or vendor.
    """
    ROLE_CHOICES = (
        ("vendor", "Vendor"),
        ("buyer", "Buyer"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        """
        Makes the username and role more readable.
        """
        return f"{self.username} ({self.role})"
