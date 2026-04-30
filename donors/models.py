from django.db import models
from django.conf import settings #to access the settings.AUTH_USER_MODEL
from django.core.exceptions import ValidationError

# Create your models here.

class DonorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #creates one to one relation
    BLOOD_GROUP = (
        ('A+','A+'),('B+','B+'),('AB+','AB+'),('O+','O+'),
        ('A-','A-'),('B-','B-'),('AB-','AB-'),('O-','O-'),
    )
    blood_group = models.CharField(max_length=5,choices=BLOOD_GROUP)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True,blank=True)
    GENDER_CHOICES = (
        ('female','Female'),('male','Male'),('others','Others'),
    )
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    height=models.FloatField()
    weight=models.FloatField()
    DEPARTMENT_CHOICES = (
        ('maths','Maths'),('computer science','Computer Science'),
        ('commerce','Commerce'),('zoology','Zoology'),
        ('botony','Botony'),('statistics','Statistics'),('physics','Physics'),
        ('chemistry','Chemistry'),('english','English'),
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True)
    phone_number = models.CharField(max_length=10)

#to check eligiblity
def is_eligible(self):
    if not self.last_donation_date:
        return True
    from datetime import datetime
    return (date.today() - self.last_donation_date.days >=90)

# to check age
def is_adult(self):
    from datetime import datetime
    today = date.today()
    age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month,self.date_of_birth.day)
    )
    if age<18:
        raise ValidationError("Donor must be atleast 18 years old.")

    if self.weight <50:
        raise ValidationError("weight must be greater than 50kg.")


#filters for matching - can include city also
class Meta:
    indexes = [
        models.Index(fields=['blood_group']),
        models.Index(fields=['available']),
    ]