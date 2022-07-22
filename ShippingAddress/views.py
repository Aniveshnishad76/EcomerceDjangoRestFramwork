from rest_framework import generics, status
from rest_framework.response import Response

from ShippingAddress.models import Shipping
from ShippingAddress.serializer import MyAddressSerializer


class CreateShipping(generics.ListCreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = MyAddressSerializer

    def get_queryset(self):
        return Shipping.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


