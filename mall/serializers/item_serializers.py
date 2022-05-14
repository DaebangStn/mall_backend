from rest_framework import serializers
from mall.models import Item, Category


class ItemSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = '__all__'
