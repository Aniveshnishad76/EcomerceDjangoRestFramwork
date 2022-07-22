import json

from rest_framework import generics, status
from rest_framework.response import Response

from AddToCart.models import Cart, CartItems
from AddToCart.serializers import MyCartSerializer, MyCartdetailsSerializer, MyCartItemsSerializer
from AdminPortal.models import Worships


class MyCart(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = MyCartSerializer

    def list(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=self.request.user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = MyCartItemsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        data = CartItems.objects.get(id=request.data['id'])
        if data:
            data.quantity = request.data['quantity']
            data.price = data.price * request.data['quantity']
            data.save()
            cart, _ = Cart.objects.get_or_create(user=self.request.user, ordered=False)
            total_price = 0
            cart_items = CartItems.objects.filter(user=self.request.user, cart=cart.id)
            for items in cart_items:
                total_price = total_price + items.price
            cart.total_price = total_price
            cart.save()
            return Response({"result": "Quantity updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"result": "This is not in Cart"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            data = CartItems.objects.get(id=request.data['id'])
            data.delete()
            total_price = 0
            cart, _ = Cart.objects.get_or_create(user=self.request.user, ordered=False)
            cart_items = CartItems.objects.filter(user=self.request.user, cart=cart.id)
            for items in cart_items:
                total_price = total_price + items.price
            cart.total_price = total_price
            cart.save()
        except:
            return Response({"result": "Please provide valid ID"}, status=status.HTTP_200_OK)
        cart = Cart.objects.filter(user=self.request.user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = MyCartItemsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyCartDetails(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = MyCartdetailsSerializer

    def create(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=self.request.user, ordered=False)
        item = Worships.objects.get(slug=kwargs.get('slug'))
        price = item.price
        quantity = request.data['quantity']
        if CartItems.objects.filter(user=self.request.user, item=item).exists():
            return Response({"result": "Already added in cart"}, status=status.HTTP_400_BAD_REQUEST)
        details = CartItems(user=self.request.user, cart=cart, item=item, price=price, quantity=quantity)
        details.save()
        total_price = 0
        cart_items = CartItems.objects.filter(user=self.request.user, cart=cart.id)
        for items in cart_items:
            total_price = total_price + items.price
        cart.total_price = total_price
        cart.save()
        return Response({"result": "Item added in cart"}, status=status.HTTP_200_OK)
