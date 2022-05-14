from mall.models import Item
from mall.serializers import ItemSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
