from django.db import models
from donors.models import DonorProfile
from requests.models import BloodRequest

# Create your models here.
class MatchingService:
    @staticmethod # doesnot depend on class instances.
    def find_donors(blood_group):
        return DonorProfile.objects.filter(
            blood_group=blood_group,
            available=True
        )