from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserAddresses(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user= models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,verbose_name='Fullname',primary_key=True,default="Full Name")
    ad_P = models.CharField(max_length=100,verbose_name='Address 1')
    ad_P2 = models.CharField(max_length=100,verbose_name='Address 2',blank=True,null=True)
    ad_City = models.CharField(max_length=100,verbose_name='City')
    ad_State = models.CharField(max_length=2,verbose_name='State')
    ad_Zip = models.CharField(max_length=5,verbose_name='Zip code')
    ad_full = models.CharField(max_length=200,default=ad_P)

    def __str__(self):
        """String for representing the Model object."""
        return self.full_name


class UserQuotes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reqGallons = models.CharField(max_length=10)
    reqDelDate = models.DateField()



