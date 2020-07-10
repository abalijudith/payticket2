from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Agence(models.Model):
    name=models.CharField(_("agence name"), max_length=250)
    owner=models.ForeignKey(User,related_name="agence_owner", on_delete=models.CASCADE)
    address=models.TextField()
    city=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.EmailField()
    logo=models.TextField()


    def __str__(self):
        return self.name



class Station(models.Model):
    title=models.CharField(max_length=250)
    agency=models.ForeignKey(Agence,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=250,blank=True,null=True)
    city=models.CharField(max_length=250)


class Trip(models.Model):
    start=models.CharField(max_length=250)
    destination=models.CharField(max_length=250)
    tripday=models.DateTimeField()
    price=models.CharField(max_length=20)
    station=models.ForeignKey(Station,on_delete=models.CASCADE)