from django.db import models

# Create your models here.
class UserData(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100,default='',unique=True)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	gender = models.CharField(max_length=6)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	pincode = models.IntegerField()
	email=models.CharField(max_length=100)
	dob = models.DateField()
	contact = models.BigIntegerField()
	password = models.CharField(max_length=100,default='')


class Room(models.Model):
	name= models.CharField(max_length=20)

class Chat(models.Model): 
	uid = models.IntegerField()
	chat = models.CharField(max_length=5000)
	roomid = models.IntegerField()
