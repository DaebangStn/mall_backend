from rest_framework import serializers
from mall.models import Category


class CategorySerializers(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)

    class Meta:
        model = Category
        fields = '__all__'
