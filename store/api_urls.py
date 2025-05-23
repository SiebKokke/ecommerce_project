from rest_framework.routers import DefaultRouter
from .views_api import StoreViewSet, ProductViewSet
from reviews.views_api import ReviewViewSet

router = DefaultRouter()
router.register("stores", StoreViewSet, basename="store")
router.register("products", ProductViewSet, basename="product")
router.register("reviews", ReviewViewSet, basename="review")

urlpatterns = router.urls
