from django.db import models

from AddToCart.models import Cart
from portal.models import UserInfo


class Orders(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=200, blank=False)
    payment_id = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.first_name}'s {self.order_id}"


class OrderItems(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
