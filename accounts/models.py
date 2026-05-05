from django.db import models

# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser

# database value and human readable input into a tuple ROLE_CHOICES
class User(AbstractUser):
    ROLE_CHOICES=(
        ('donor','Donor'),
        ('hospital','Hospital'),
        ('admins','Admins'),
    )
    #creates a new column in user table 
    role=models.CharField(max_length=10,choices=ROLE_CHOICES, default='donor')

class Admin(models.Model):
    username=models.CharField(max_length=100,default="Admin123")
    password=models.CharField(max_length=100,default="Admin123")
    email = models.EmailField(blank=True, null=True)