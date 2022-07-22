from rest_framework import serializers

from AdminPortal.models import Worships


class CreateWorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worships
        fields = ('slug', 'title', 'description', 'start_time', 'end_date', 'images', 'is_available','price')


class GetBySlug(serializers.ModelSerializer):
    class Meta:
        model = Worships
        fields = ('slug', 'title', 'description', 'start_time', 'end_date', 'images', 'is_available', "price")

