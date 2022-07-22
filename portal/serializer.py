from rest_framework import serializers

from portal.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'profile', "is_premium",
                  'id', 'email', 'last_login', "is_superuser", "is_staff", "date_joined","is_verified"]
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = (
            'id', 'email', 'last_login', "is_superuser", "is_staff", "date_joined", "password",
            "is_verified","groups", "user_permissions")

