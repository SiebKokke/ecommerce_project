from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.contrib import messages


# This file contains decorators for rolebased access
# control in a Django application.
def role_required(role):
    """
    Decorator to check if the user has the required role.
    """
    def decorator(view_func):
        """
        Decorator to wrap the view function.
        """
        def _wrapped_view(request, *args, **kwargs):
            """
            Wrapper function to check the user's role.
            """
            if not request.user.is_authenticated:
                return redirect("login")
            if request.user.role != role:
                messages.error(
                    request, "You do not have permission to access this page."
                )
                if request.user.role == "vendor":
                    return redirect("vendor_dashboard")
                elif request.user.role == "buyer":
                    return redirect("buyer_dashboard")
                else:
                    return redirect("home")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
