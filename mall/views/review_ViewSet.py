from mall.models import Review
from mall.serializers import ReviewSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
