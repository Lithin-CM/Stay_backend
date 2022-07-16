from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserRegistration(AbstractUser):
    phone_number = models.CharField(max_length=10,unique=True,null=True)
    email = models.CharField(max_length=50,unique=True)
    gender = models.CharField(max_length=10)
    is_hostel = models.BooleanField(default=False)

    def __str__(self):
       return str(self.username)
   

