from mall.models import Category
from mall.serializers import CategorySerializers
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryRootView(generics.ListAPIView):
    serializer_class = CategorySerializers

    def get_queryset(self):
        return Category.objects.filter(parent=None)


class CategorySubView(generics.ListAPIView):
    serializer_class = CategorySerializers

    def get_queryset(self):
        parent_slug = self.kwargs['category']
        return Category.objects.filter(parent__slug=parent_slug)