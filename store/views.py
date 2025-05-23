from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StoreForm, ProductForm
from .models import Store, Product
from core.decorators import role_required
from core.twitter_utils import post_tweet


# The next classes are for the store management on vendor side.
@role_required("vendor")
@login_required
def store_list(request):
    """
    Displays a list of stores owned by the logged-in user.
    """
    stores = Store.objects.filter(owner=request.user)
    return render(request, "store/store_list.html", {"stores": stores})


@role_required("vendor")
@login_required
def store_create(request):
    """
    Creates a new store for the logged-in user.
    """
    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            tweet_text = f"New store added: {store.name}\n{store.description}"
            # No logo path since I could not access actual API
            logo_path = (
                store.logo.path if (
                    hasattr(store, "logo") and store.logo
                ) else None
            )
            post_tweet(tweet_text, logo_path)
            return redirect("store_list")
    else:
        form = StoreForm()
    return render(request, "store/store_form.html", {"form": form})


@role_required("vendor")
@login_required
def store_edit(request, pk):
    """
    Edits an existing store owned by the logged-in user.
    """
    store = get_object_or_404(Store, pk=pk, owner=request.user)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect("store_list")
    else:
        form = StoreForm(instance=store)
    return render(request, "store/store_form.html", {"form": form})


@role_required("vendor")
@login_required
def store_delete(request, pk):
    """
    Deletes a store owned by the logged-in user.
    """
    store = get_object_or_404(Store, pk=pk, owner=request.user)
    if request.method == "POST":
        store.delete()
        return redirect("store_list")
    return render(request, "store/store_confirm_delete.html", {"store": store})


# The next classes are for the product management on vendor side.

@role_required("vendor")
@login_required
def product_list(request, store_id):
    """
    This view displays a list of products for a specific store.
    """
    store = get_object_or_404(Store, pk=store_id, owner=request.user)
    products = Product.objects.filter(store=store)
    return render(
        request,
        "store/product_list.html",
        {"store": store, "products": products},
    )


@role_required("vendor")
@login_required
def product_create(request, store_id):
    """
    This view allows the vendor to create a new product for their store.
    """
    store = get_object_or_404(Store, id=store_id, owner=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            tweet_text = (
                f"New product added in {product.store.name}!\n"
                f"Product: {product.name}\n"
                f"{product.description}"
            )
            image_path = (
                product.image.path
                if hasattr(product, "image") and product.image
                else None
            )
            post_tweet(tweet_text, image_path)
            return redirect("product_list", store_id=store.pk)
    else:
        form = ProductForm()
    return render(
        request,
        "store/product_form.html",
        {"form": form, "store": store},
    )


@role_required("vendor")
@login_required
def product_edit(request, store_id, product_id):
    """
    This view allows the vendor to edit an existing product in their store.
    """
    store = get_object_or_404(Store, pk=store_id, owner=request.user)
    product = get_object_or_404(Product, pk=product_id, store=store)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list", store_id=store.pk)
    else:
        form = ProductForm(instance=product)
    return render(
        request,
        "store/product_form.html",
        {"form": form, "store": store},
    )


@role_required("vendor")
@login_required
def product_delete(request, store_id, product_id):
    """
    This view allows the vendor to delete a product from their store.
    """
    store = get_object_or_404(Store, pk=store_id, owner=request.user)
    product = get_object_or_404(Product, pk=product_id, store=store)
    if request.method == "POST":
        product.delete()
        return redirect("product_list", store_id=store.pk)
    return render(
        request,
        "store/product_confirm_delete.html",
        {"product": product, "store": store},
    )


def product_detail(request, product_id):
    """
    Shows detailed info about a product, including reviews.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    return render(request, "store/product_detail.html", {
        "product": product,
        "reviews": reviews
    })


# This view is for the product catalog on the buyer side.
@login_required
def product_catalog(request):
    """
    Displays a catalog of all products available in the store.
    """
    products = Product.objects.all()
    return render(
        request,
        "store/product_catalog.html",
        {"products": products}
    )
