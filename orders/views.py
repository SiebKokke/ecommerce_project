from django.shortcuts import render, redirect
from store.models import Product
from .models import Order, OrderItem
from core.decorators import role_required
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


@role_required("buyer")
@login_required
def add_to_cart(request, product_id):
    """
    Adds a product to the user's cart.
    Uses session to store cart items.
    """
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    return redirect("product_catalog")


@role_required("buyer")
@login_required
def view_cart(request):
    """
    Displays the user's shopping cart.
    """
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        if str(product.id) in cart:
            quantity = cart[str(product.id)]
        else:
            quantity = cart[product.id]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })
    return render(
        request,
        "orders/cart.html",
        {"cart_items": cart_items, "total": total},
    )


# This view is for the checkout process
@role_required("buyer")
@login_required
def checkout(request):
    """
    Handles the checkout process.
    This view is responsible for processing the user's order.
    """
    cart = request.session.get("cart", {})
    if not cart:
        return redirect("view_cart")
    order = Order.objects.create(buyer=request.user)
    total = 0
    products = Product.objects.filter(id__in=cart.keys())
    for product in products:
        quantity = cart[str(product.id)]
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )
        """
        Reduces the inventory count of the product.
        """
        product.inventory_count -= quantity
        product.save()
        total += product.price * quantity
    request.session["cart"] = {}
    request.session.modified = True
    """
    Sends an email to the user with the order summary.
    """
    subject = "Your Invoice from E-Commerce Store"
    message = f"Thank you for your purchase, {request.user.username}!\n\n"
    message += "Order Summary:\n"
    for item in order.items.all():
        message += f"{item.product.name}: {item.quantity} x ${item.price}\n"
    message += f"\nTotal: ${total}\n"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [request.user.email],
        fail_silently=False,
    )

    return render(request, "orders/checkout_success.html", {"order": order})
