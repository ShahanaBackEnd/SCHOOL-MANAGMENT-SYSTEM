from django.db import models
from authentication.models import CustomUser


class role(models.Model):
    name = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=120)


class State(models.Model):
    name = models.CharField(max_length=120)
    country_id = models.ForeignKey(Country,on_delete=models.DO_NOTHING)    


class City(models.Model):
    name = models.CharField(max_length=120)
    state_id = models.ForeignKey(State,on_delete=models.DO_NOTHING)
    



class Address(models.Model):
    user_id =models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    house_no = models.IntegerField()
    area_code = models.IntegerField()
    country_id = models.OneToOneField(Country,on_delete=models.DO_NOTHING)
    state_id = models.OneToOneField(State, on_delete=models.DO_NOTHING)
    city_id = models.OneToOneField(City,on_delete=models.DO_NOTHING)
    address_line = models.CharField(max_length=250)
    

class  Director(models.Model):
    user_id = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=250,null=False)
    gender = models.CharField(max_length=50)


class Banking_Details(models.Model):
    account_no = models.BigIntegerField(primary_key=True , unique=True)
    IFSC_code = models.BigIntegerField()
    holder_name = models.CharField(max_length=255)
    user_id = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING)

class School_Year(models.Model):
    year_name = models.CharField(max_length=250)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)


class Year_Level(models.Model):
    level_name = models.CharField(max_length=250)
    level_order = models.IntegerField()


class Term (models.Model):
    year_id= models.ForeignKey(School_Year, on_delete=models.DO_NOTHING)
    term_number = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()


class Period (models.Model):
    year_id = models.ForeignKey(School_Year , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    start_time = models.TimeField()
    end_time = models.TimeField()



class Department(models.Model):
    department_name = models.CharField(max_length=250,null=False) 



class Subject(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    subject_name = models.CharField(max_length=200,null=False)


class classroom_type(models.Model):
    Name = models.CharField(max_length=255,null=False)


class Classroom(models.Model):
    room_type_id = models.ForeignKey(classroom_type,blank=True,null=True,on_delete=models.DO_NOTHING)
    room_name = models.CharField(max_length=200)
    capacity = models.IntegerField()



