from django.db import models
from director.models import Subject,Term,Period,Classroom,Year_Level,School_Year
from authentication.models import CustomUser
from teacher.models import *
# from director.models import Class_period


class Student (models.Model):
    user_id = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField(null=False)
    gender = models.CharField(max_length=50)
    enrollment_date =  models.DateField(null=False)

##-----Relation between Student and Class_period(ManytoMany Relatonship)--------

    classes = models.ManyToManyField('Class_Period', blank=False,related_name='Student')

class Guardian(models.Model):
    user_id = models.IntegerField()
    phone_number = models.CharField(max_length=50,null=False)


class Guardian_type(models.Model):
    name = models.CharField(max_length=255,null=False)

    
##-----Relation between Student, Gaurdian and Guardian_type(OnetoMany Relatonship)--------
class Student_Guardian(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    guardian = models.ForeignKey(Guardian,on_delete=models.DO_NOTHING)
    guardian_type_id = models.ForeignKey( Guardian_type,on_delete=models.DO_NOTHING)


class Class_Period(models.Model):
    name=models.CharField(max_length=250)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    term_id = models.ForeignKey(Term,on_delete=models.DO_NOTHING)
    start_period_id = models.ForeignKey(Period,on_delete=models.DO_NOTHING,related_name='start_time_set')
    end_period_id=models.ForeignKey(Period,on_delete=models.DO_NOTHING, related_name='end_time_set')
    classroom_id = models.ForeignKey(Classroom,on_delete=models.DO_NOTHING)


class Student_Year_Level(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    level_id=models.ForeignKey(Year_Level, on_delete=models.DO_NOTHING)
    year_id= models.ForeignKey(School_Year,on_delete=models.DO_NOTHING)