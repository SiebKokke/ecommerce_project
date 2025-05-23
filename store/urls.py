from django.urls import path
from . import views


# URL patterns for the store app
urlpatterns = [
    path("vendor/stores/", views.store_list, name="store_list"),
    path("vendor/stores/create/", views.store_create, name="store_create"),
    path("vendor/stores/<int:pk>/edit/", views.store_edit, name="store_edit"),
    path(
        "vendor/stores/<int:pk>/delete/",
        views.store_delete,
        name="store_delete",
    ),
    path(
        "vendor/stores/<int:store_id>/products/",
        views.product_list,
        name="product_list",
    ),
    path(
        "vendor/stores/<int:store_id>/products/create/",
        views.product_create,
        name="product_create",
    ),
    path(
        "vendor/stores/<int:store_id>/products/<int:product_id>/edit/",
        views.product_edit,
        name="product_edit",
    ),
    path(
        "vendor/stores/<int:store_id>/products/<int:product_id>/delete/",
        views.product_delete,
        name="product_delete",
    ),
    path("products/", views.product_catalog, name="product_catalog"),
    path(
        "products/<int:product_id>/",
        views.product_detail,
        name="product_detail",
    ),
]
