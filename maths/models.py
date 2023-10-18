from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='maths_users_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='maths_users_permissions')

class About(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    school = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20) 



