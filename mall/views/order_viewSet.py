from mall.models import Order
from mall.serializers import OrderSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
