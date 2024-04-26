from django.db import models
from authentication.models import CustomUser

class Teacher(models.Model):
    User_id =models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
    Phone_no = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Adhaar_no = models.BigIntegerField()
    Pan_no = models.BigIntegerField()
    Qualification = models.CharField(max_length=250) 
