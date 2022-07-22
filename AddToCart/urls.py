from django.urls import path

from AddToCart.views import MyCart, MyCartDetails

urlpatterns = [
    path('my-cart/', MyCart.as_view(), name="my-cart"),
    path('<slug>', MyCartDetails.as_view(), name="my-cart-details"),
]
