from rest_framework import serializers
from mall.models import Account


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['password',]

