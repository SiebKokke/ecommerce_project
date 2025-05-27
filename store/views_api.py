from rest_framework import permissions, viewsets
from .models import Store, Product
from .serializers import StoreSerializer, ProductSerializer


class IsVendor(permissions.BasePermission):
    """
    Custom permission to only allow vendors to edit or delete their stores
    and products.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, "role", None) == "vendor"
        )


class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stores to be viewed or edited.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsVendor()]
        return [permissions.AllowAny()]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsVendor()]
        return [permissions.AllowAny()]
