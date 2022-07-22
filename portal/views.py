from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from AdminPortal.models import Worships
from portal.models import UserInfo
from portal.serializer import UserInfoSerializer, UserUpdateSerializer


class Signup(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return UserInfo.objects.filter(email=self.request.user)


class UserRetrieve(generics.UpdateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return Response({"result": "User deleted successfully"}, status=status.HTTP_200_OK)












