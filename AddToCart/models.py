from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from djmoney.models.fields import MoneyField
from re import sub
from decimal import Decimal
from AdminPortal.models import Worships
from portal.models import UserInfo


class Cart(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.total_price} of {self.user.first_name}"


class CartItems(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Worships, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.first_name} cart with {self.price}"


@receiver(pre_save, sender=CartItems)
def price_calculations(sender, **kwargs):
    cart_items = kwargs['instance']
    worships = Worships.objects.get(id=cart_items.item.id)
    cart_items.price = cart_items.quantity * worships.price
