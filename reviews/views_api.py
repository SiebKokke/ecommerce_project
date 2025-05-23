from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from core.twitter_utils import post_tweet

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
