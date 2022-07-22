from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from AdminPortal.models import Worships
from AdminPortal.serializer import CreateWorshipSerializer, GetBySlug


class CreateWorship(generics.ListCreateAPIView):
    queryset = Worships.objects.all()
    serializer_class = CreateWorshipSerializer


class ArticleDetailView(generics.ListAPIView, generics.DestroyAPIView):
    queryset = Worships.objects.all()
    serializer_class = GetBySlug

    def get_queryset(self):
        queryset = Worships.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def delete(self, request, *args, **kwargs):
        worship = self.get_queryset()
        if worship:
            worship.delete()
            return Response({"result": "Deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"result": "No data found"}, status=status.HTTP_404_NOT_FOUND)
