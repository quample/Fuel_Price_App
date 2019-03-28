from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserAddresses(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user= models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,blank=True,null=True)
    full_name = models.CharField(max_length=50,verbose_name='Full Name',primary_key=True,default="Full Name")
    ad_P = models.CharField(max_length=100,verbose_name='Address 1')
    ad_P2 = models.CharField(max_length=100,verbose_name='Address 2',blank=True,null=True)
    ad_City = models.CharField(max_length=100,verbose_name='City')
    ad_State = models.CharField(max_length=2,verbose_name='State')
    ad_Zip = models.CharField(max_length=5,verbose_name='Zip code')
    ad_full = models.CharField(max_length=250,default=ad_P)

    def __str__(self):
        """String for representing the Model object."""
        return self.full_name
    def combo_address(self):
        ad_full = "%s , %s, %s, %s %s" % (self.ad_P,self.ad_P2,self.ad_City,self.ad_State,self.ad_Zip)
        return self.ad_full


class UserQuotes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,blank=True,null=True)
    order_Num = models.AutoField(primary_key=True,default=0)
    reqGallons = models.CharField(max_length=10,verbose_name="Requested Gallons")
    reqDelDate = models.DateField(verbose_name="Delivery Date",default="YYYY-MM-DD")

    def __str__(self):
        return self.order_Num



