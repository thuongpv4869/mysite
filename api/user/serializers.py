from rest_framework import serializers

from core.models.user import UserFullInfo


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFullInfo
        fields = ['id', 'email', 'first_name', 'last_name', 'date_of_birth']
