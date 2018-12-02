from rest_framework import serializers
from .models import Alliance
from mainPage.serializers import UserSerializer


class AllianceSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Alliance
        fields = ('name', 'creator', 'vice_creator', 'alliance_logo', 'alliance_bio', 'members')

