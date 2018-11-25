from rest_framework import serializers
from .models import CityOwned


class CityOwnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityOwned
        fields = '__all__'
