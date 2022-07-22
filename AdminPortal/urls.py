from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from AdminPortal import views
from AdminPortal.views import CreateWorship, ArticleDetailView

urlpatterns = [
    path('worship/', CreateWorship.as_view(), name="CreateWorship"),
    path('<slug:slug>', ArticleDetailView.as_view(),name="worship_details")
]


