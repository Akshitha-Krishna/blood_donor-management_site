
from rest_framework import serializers
from .models import DonorProfile

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = '__all__'