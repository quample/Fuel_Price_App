from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserQuotes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reqGallons = models.CharField(max_length=10)
    reqDelDate = models.DateField()