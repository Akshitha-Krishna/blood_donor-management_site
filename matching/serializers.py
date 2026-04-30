
from rest_framework import serializers
from .models import MatchingService

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingService
        fields = '__all__'
        