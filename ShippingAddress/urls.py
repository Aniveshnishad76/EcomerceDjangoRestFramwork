from django.urls import path

from ShippingAddress.views import CreateShipping

urlpatterns = [
    path('', CreateShipping.as_view(), name="shipping")
]
