from django.db import models
from django.conf import settings

# Create your models here.

class Hospital(models.Model):
    user = models.OneToOneField('accounts.User',on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
