from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator 
# Create your models here.
def min_len(value):
    if len(value) < 5:
        raise ValidationError(
        _('%(value)s is below minimum zip code length'),
        params={'value': value},
        )   

class UserAddresses(models.Model):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alpha characters are allowed.')
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user= models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,blank=True,null=True)
    full_name = models.CharField(max_length=50,verbose_name='Full Name',primary_key=True)
    ad_P = models.CharField(max_length=100,verbose_name='Address 1')
    ad_P2 = models.CharField(max_length=100,verbose_name='Address 2',blank=True,null=True)
    ad_City = models.CharField(max_length=100,verbose_name='City',validators=[alpha])
    ad_State = models.CharField(max_length=2,verbose_name='State',validators=[alpha])
    ad_Zip = models.CharField(max_length=9,verbose_name='Zip code',validators=[min_len, numeric])
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
    reqGallons = models.FloatField(verbose_name="Requested Gallons")
    reqDelDate = models.DateField(blank=False,verbose_name="Delivery Date",default="MM/DD/YYYY")
    delivery_address = models.CharField(max_length=300,verbose_name="Delivery Address")
    pricePerGal = models.FloatField(blank=False,verbose_name="Suggested Price",default='0.00')
    totalPrice = models.FloatField(blank=False,verbose_name="Total Price",default='0.00')

    def __str__(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        if ', TX' in self.delivery_address:
            locationrate = 0.02
            print("locationrate:",locationrate)
            #self.pricePerGal = 5.0
        else:
            locationrate = 0.04
            print("locationrate:",locationrate)
            #self.pricePerGal = 10.0

        # if user has ordered before
        if UserQuotes.objects.filter(user_name=self.user_name).count() >= 1:
            historyrate = 0.01
            print(User.username)
            print("historyrate:",historyrate)
        # else
        else:
            historyrate = 0.0
            print("historyrate:",historyrate)
            print(User.username)
        # gallons rates
        if self.reqGallons > 1000:
            gallonsrate = 0.02
            print("gallonsrate:",gallonsrate)
        else:
            gallonsrate = 0.03
            print("gallonsrate:",gallonsrate)
        profitfactor = 0.1

        # season rates NOT FINISHED

        # if summer
        month = self.reqDelDate.strftime("%B")
        if month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August':
            seasonrate = 0.04
            print("seasonrate :",seasonrate)
        else:
            seasonrate = 0.03
            print("seasonrate :",seasonrate)

            
        pricepergallon = 1.50 + (locationrate - historyrate + gallonsrate + profitfactor + seasonrate) * 1.50
        total = self.reqGallons * pricepergallon

        self.pricePerGal = pricepergallon
        self.totalPrice = total
        super(UserQuotes, self).save(*args, **kwargs)
