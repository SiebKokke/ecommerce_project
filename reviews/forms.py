from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating and updating review instances.
    """
    class Meta:
        model = Review
        fields = ["content", "rating"]