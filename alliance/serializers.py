from rest_framework import serializers
from .models import Alliance


class AllianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alliance
        fields = '__all__'

