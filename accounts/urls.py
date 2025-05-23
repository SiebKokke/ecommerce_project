from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RoleBasedLoginView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", RoleBasedLoginView.as_view(), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path("", views.home, name="home"),
    path("vendor/dashboard/", views.vendor_dashboard, name="vendor_dashboard"),
    path("buyer/dashboard/", views.buyer_dashboard, name="buyer_dashboard"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),]
