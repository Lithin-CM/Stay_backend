from django.db import models
from cloudinary.models import CloudinaryField
from user.models import *



# Create your models here.

class Hostels(models.Model):
    owner = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    Hostel_name = models.CharField(max_length=50)
    Hostel_type = models.CharField(max_length=10,null=True)
    location = models.CharField(max_length=200)
    rating = models.FloatField(null=True)
    food = models.BooleanField(default=False)
    pg = models.BooleanField(default=False)
    image = CloudinaryField('image')
    details = models.CharField(max_length=500,null=True)
    facility1 = models.CharField(max_length=50,null=True)
    facility2 = models.CharField(max_length=50,null=True)
    facility3 = models.CharField(max_length=50,null=True)
    facility4 = models.CharField(max_length=50,null=True)
    facility5 = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.Hostel_name)


class HostelImages(models.Model):
    hostel = models.ForeignKey(Hostels, on_delete=models.CASCADE)
    image = CloudinaryField('image')




class Rooms(models.Model):
    hostel = models.ForeignKey(Hostels, on_delete=models.CASCADE)
    roomCatecoryName = models.CharField(max_length=100)
    sharing = models.IntegerField()
    roomCount = models.IntegerField()
    amountFor_10_days = models.IntegerField()
    amountFor_20_days = models.IntegerField()
    amountFor_a_month = models.IntegerField()
    rating = models.FloatField()
    image = CloudinaryField('image')
    details = models.CharField(max_length=500,null=True)


class HostelRoomImages(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    image =CloudinaryField('image')


class Reviews(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostels, on_delete=models.CASCADE)
    text = models.CharField(max_length= 250)
    stars = models.FloatField()
    

class ReviewsForRooms(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    Room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    text = models.CharField(max_length= 250)
    stars = models.FloatField()

    

