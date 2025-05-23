from django.urls import path
from . import views


# URL patterns for the reviews app
urlpatterns = [
    path(
        "products/<int:product_id>/add_review/",
        views.add_review,
        name="add_review",
    ),
]
