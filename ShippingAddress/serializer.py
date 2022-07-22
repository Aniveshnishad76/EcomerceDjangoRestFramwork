from rest_framework import serializers

from ShippingAddress.models import Shipping
from portal.serializer import UserUpdateSerializer


class MyAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping
        fields = "__all__"
