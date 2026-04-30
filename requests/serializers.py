
from rest_framework import serializers
from .models import BloodRequest

class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = '__all__'