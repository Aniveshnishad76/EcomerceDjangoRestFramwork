from django.contrib import admin

from OrderCreation.models import Orders
from wishlist.models import WishList

admin.site.register(WishList)
admin.site.register(Orders)