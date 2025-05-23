from django.urls import path
from . import views


# URL patterns for the orders app
urlpatterns = [
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),
    path("checkout/", views.checkout, name="checkout"),
]
