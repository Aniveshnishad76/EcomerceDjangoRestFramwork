from django.urls import path

from OrderCreation.views import OrderList

urlpatterns =[
    path("",OrderList.as_view(),name="orders"),
]