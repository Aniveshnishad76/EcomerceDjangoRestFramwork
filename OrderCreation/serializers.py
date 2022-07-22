from rest_framework import serializers

from AddToCart.serializers import MyCartSerializer
from OrderCreation.models import Orders, OrderItems


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"


class MyOrderItemsSerializer(serializers.ModelSerializer):
    cart = MyCartSerializer()

    class Meta:
        model = OrderItems
        fields = "__all__"
