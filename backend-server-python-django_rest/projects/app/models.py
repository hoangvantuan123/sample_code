from django.db import models
from django.contrib.auth.models import make_password

# Create your models here.
class Users(models.Model):

    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        # Save the email address 
        self.password = kwargs.pop('password',self.password)
        super(Users, self).save(*args, **kwargs)


class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)