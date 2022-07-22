from django.db import models

from AdminPortal.models import Worships
from portal.models import UserInfo


class WishList(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    item = models.ForeignKey(Worships, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.item.slug} of {self.user.first_name}"
