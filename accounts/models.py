from django.db import models

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