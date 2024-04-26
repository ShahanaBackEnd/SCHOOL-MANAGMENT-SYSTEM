from django.db import models
# from django.conf import settings
# from director.models import role
from django.contrib.auth.models import AbstractUser,PermissionsMixin

class CustomUser(AbstractUser,PermissionsMixin):
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, null=False)
    password=models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    

    # role = models.ManyToManyField('director.role', blank=True,related_name='user')

    