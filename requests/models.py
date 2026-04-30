from django.db import models
from hospitals.models import Hospital

# Create your models here.
class BloodRequest(models.Model):
    STATUS = (
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    )

    hospital = models.ForeignKey('hospitals.Hospital',on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=10)
    urgency =models.CharField(max_length=10)
    status = models.CharField(max_length=20,choices=STATUS, default='pending')
    created_at = models.DateField(auto_now_add=True)

