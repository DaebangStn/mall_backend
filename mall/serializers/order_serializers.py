from rest_framework import serializers
from mall.models import Order, Account


class OrderSerializers(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    shipping_address = serializers.SerializerMethodField()

    # TODO("Though the other address is typed, the default value occupies.")
    def default_shipping_address(self, obj):
        return obj.account.default_address

    class Meta:
        model = Order
        fields = '__all__'
