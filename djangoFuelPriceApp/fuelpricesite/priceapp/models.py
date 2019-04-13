from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
def min_len(value):
    if len(value) < 5:
        raise ValidationError(
        _('%(value)s is below minimum zip code length'),
        params={'value': value},
        )   

class UserAddresses(models.Model):

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user= models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,blank=True,null=True)
    full_name = models.CharField(max_length=50,verbose_name='Full Name',primary_key=True)
    ad_P = models.CharField(max_length=100,verbose_name='Address 1')
    ad_P2 = models.CharField(max_length=100,verbose_name='Address 2',blank=True,null=True)
    ad_City = models.CharField(max_length=100,verbose_name='City')
    ad_State = models.CharField(max_length=2,verbose_name='State')
    ad_Zip = models.CharField(max_length=9,verbose_name='Zip code',validators=[min_len])
    ad_full = models.CharField(max_length=250,default=ad_P)

    def __str__(self):
        """String for representing the Model object."""
        return self.full_name

    def save(self, *args, **kwargs):
        if self.ad_P2 is not None:

            self.ad_full = "%s , %s, %s, %s %s" % (self.ad_P,self.ad_P2,self.ad_City,self.ad_State,self.ad_Zip)
        else:
            self.ad_full = "%s , %s, %s %s" % (self.ad_P,self.ad_City,self.ad_State,self.ad_Zip)
        super(UserAddresses, self).save(*args, **kwargs)

class UserQuotes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,blank=True,null=True)
    order_id = models.AutoField(primary_key=True)
    reqGallons = models.CharField(max_length=10,verbose_name="Requested Gallons")
    reqDelDate = models.DateField(blank=False,verbose_name="Delivery Date",default="MM/DD/YYYY")
    delivery_address = models.CharField(max_length=300,verbose_name="Delivery Address")

    def __str__(self):
        return str(self.order_id)
'''
class Competitor_price2017(models.Model):
    competitor_name = models.CharField(max_length=100,blank=True,primary_key=True)
    Jan = models.SmallIntegerField()
    Feb = models.SmallIntegerField()
    Mar = models.SmallIntegerField()
    Apr = models.SmallIntegerField()
    May = models.SmallIntegerField()
    Jun = models.SmallIntegerField()
    Jul = models.SmallIntegerField()
    Aug = models.SmallIntegerField()
    Sep = models.SmallIntegerField()
    Oct = models.SmallIntegerField()
    Nov = models.SmallIntegerField()
    Dec = models.SmallIntegerField()

class Competitor_price2018(models.Model):
    competitor_name = models.CharField(max_length=100,blank=True,primary_key=True)
    Jan = models.SmallIntegerField()
    Feb = models.SmallIntegerField()
    Mar = models.SmallIntegerField()
    Apr = models.SmallIntegerField()
    May = models.SmallIntegerField()
    Jun = models.SmallIntegerField()
    Jul = models.SmallIntegerField()
    Aug = models.SmallIntegerField()
    Sep = models.SmallIntegerField()
    Oct = models.SmallIntegerField()
    Nov = models.SmallIntegerField()
    Dec = models.SmallIntegerField()
'''
