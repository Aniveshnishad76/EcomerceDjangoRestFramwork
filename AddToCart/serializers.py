from rest_framework import serializers

from AddToCart.models import Cart, CartItems
from AdminPortal.serializer import CreateWorshipSerializer


class MyCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class MyCartdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class MyCartItemsSerializer(serializers.ModelSerializer):
    cart = MyCartSerializer()
    item = CreateWorshipSerializer()

    class Meta:
        model = CartItems
        fields = "__all__"
