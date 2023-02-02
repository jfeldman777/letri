from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Army(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Body(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20,blank=True,null=True)
    last_name = models.CharField(max_length=20)
    region = models.ForeignKey(Region,null=True,on_delete=models.SET_NULL)
    army = models.ForeignKey(Army,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name+ ' ' + self.last_name + ' (' + str(self.id) + ')'
