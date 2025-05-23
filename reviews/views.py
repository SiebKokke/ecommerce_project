from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .forms import ReviewForm
from orders.models import OrderItem
from core.decorators import role_required
from django.contrib.auth.decorators import login_required
# Create your views here.


@role_required("buyer")
@login_required
def add_review(request, product_id):
    """
    Allows users to add a review for a product.
    This view checks if the user has purchased the product before allowing
    them to leave a review.
    Checks if it is a verified or unverified review.
    """
    product = get_object_or_404(Product, pk=product_id)
    verified = OrderItem.objects.filter(
        order__buyer=request.user, product=product
    ).exists()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.verified = verified
            review.save()
            return redirect("product_detail", product_id=product.id)
    else:
        form = ReviewForm()
    return render(
        request,
        "reviews/add_review.html",
        {"form": form, "product": product}
    )
