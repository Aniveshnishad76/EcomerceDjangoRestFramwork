from django.db import models

from OrderCreation.models import Orders
from portal.models import UserInfo


class Shipping(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True)
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    pincode = models.PositiveIntegerField()
    landmark = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name
