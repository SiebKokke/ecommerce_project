from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.


def register(request):
    """
    Handles the registration of a new user.
    This view allows users to create an account.
    Also logs in user automatically after registration.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def home(request):
    """
    Creates the home page of the store.
    """
    if request.user.is_authenticated:
        if request.user.role == "vendor":
            return redirect("vendor_dashboard")
        elif request.user.role == "buyer":
            return redirect("buyer_dashboard")
    return render(request, "accounts/home.html")


class RoleBasedLoginView(LoginView):
    """
    Custom login view that redirects users based on their role.
    """
    template_name = "accounts/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.role == "vendor":
            return reverse("vendor_dashboard")
        elif user.role == "buyer":
            return reverse("buyer_dashboard")
        else:
            return reverse("home")


@login_required
def vendor_dashboard(request):
    """
    Dashboard for the vendors
    """
    return render(request, "accounts/vendor_dashboard.html")


@login_required
def buyer_dashboard(request):
    """
    Dashboard for the buyers
    """
    return render(request, "accounts/buyer_dashboard.html")
