import random

from rest_framework import generics, status
from rest_framework.response import Response

from AddToCart.models import Cart, CartItems
from AddToCart.serializers import MyCartItemsSerializer
from OrderCreation.models import Orders
from OrderCreation.serializers import OrderSerializer
from ShippingAddress.models import Shipping


class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        shipping_address = Shipping.objects.filter(user=self.request.user)
        if shipping_address:
            cart = Cart.objects.filter(user=self.request.user, ordered=False).first()
            ordered_id = "ORDER_ID_" + str(random.randint(1000, 9999))
            payment_id = "PAYMENT_ID_" + str(random.randint(1000, 9999))
            request.data['user'] = self.request.user.id
            request.data['cart'] = cart.id
            request.data['is_paid'] = True
            request.data['order_id'] = ordered_id
            request.data['payment_id'] = payment_id
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                cart = Cart.objects.filter(user=self.request.user,ordered=False).first()
                print(cart)
                cart.ordered = True
                cart.save()
                items = CartItems.objects.filter(user=self.request.user)
                for item in items:
                    item.delete()
                return Response({"result" : "Order created Successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result" : "Please add a shipping Address"})
