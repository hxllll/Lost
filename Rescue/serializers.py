from rest_framework import serializers

from Rescue.models import RescueUser


class RescueUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueUser
        fields = ("r_username", "r_password", "r_tel", "r_site")

    def create(self, validated_data):
        user = RescueUser()
        r_username = validated_data.get("r_username")
        user.r_username = r_username
        r_password = validated_data.get("r_password")
        user.set_password(r_password)
        r_tel = validated_data.get("r_tel")
        user.r_tel = r_tel
        r_site = validated_data.get("r_site")
        user.r_site = r_site

        user.save()
        return user
