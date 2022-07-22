from rest_framework import serializers

from AdminPortal.models import Worships
from AdminPortal.serializer import CreateWorshipSerializer
from portal.models import UserInfo
from portal.serializer import UserInfoSerializer
from wishlist.models import WishList


class WishListSerializer(serializers.ModelSerializer):
    item_details = serializers.SerializerMethodField()

    class Meta:
        model = WishList
        fields = ("item", 'item_details', "created_at")

    def get_item_details(self, obj):
        return CreateWorshipSerializer(instance=obj.item).data


class WishListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = "__all__"
