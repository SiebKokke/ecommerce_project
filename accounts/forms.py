from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    """
    Allows for the creation of a new user.
    This form is used in the registration view.
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        """
        Allows user to select a role when registering.
        """
        super().__init__(*args, **kwargs)
        self.fields["role"].widget = forms.Select(choices=User.ROLE_CHOICES)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["role"].widget = forms.Select(choices=User.ROLE_CHOICES)
