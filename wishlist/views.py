from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from AdminPortal.models import Worships
from wishlist.models import WishList
from wishlist.serializers import WishListSerializer, WishListCreateSerializer


class WishListView(generics.ListAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)


class WishListViewCreate(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListCreateSerializer

    def create(self, request, *args, **kwargs):
        item = Worships.objects.get(slug=kwargs.get('slug'))
        data = {"user": request.user.id, "item": item.id}
        if WishList.objects.filter(user=request.user.id, item=item.id).exists():
            return Response({"result": "This pooja is already in WistList"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"result": "WistListed Success"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        item = Worships.objects.get(slug=kwargs.get('slug'))

        data = WishList.objects.filter(user=self.request.user, item=item.id)
        if data:
            data.delete()
            return Response({"result": "Removed from WistList"}, status=status.HTTP_200_OK)
        else:
            return Response({"result": "This is not in WistList"}, status=status.HTTP_400_BAD_REQUEST)
