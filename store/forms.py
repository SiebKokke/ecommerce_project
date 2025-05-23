from django import forms
from .models import Store, Product


class StoreForm(forms.ModelForm):
    """
    Form for creating and updating store instances.
    """
    class Meta:
        model = Store
        fields = ["name", "description"]


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating product instances.
    """
    class Meta:
        model = Product
        fields = ["name", "description", "price", "inventory_count"]
