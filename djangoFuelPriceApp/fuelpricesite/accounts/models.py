from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAddresses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ad_P = models.CharField(max_length=100)
    ad_City = models.CharField(max_length=100)
    ad_State = models.CharField(max_length=2)
    ad_Zip = models.CharField(max_length=5)