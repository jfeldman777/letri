from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Letter(models.Model):
    first_name = models.CharField(max_length=20,blank=True,null=True)
    middle_name = models.CharField(max_length=20,blank=True,null=True)
    last_name = models.CharField(max_length=20,blank=True,null=True)
    img = models.ImageField(null=True,blank=True,upload_to='images/')
    txt = models.TextField(blank=True,null=True,)
    phone = models.CharField('Contact Phone',max_length=9,blank=True,null=True,)
    web = models.URLField('Website Address',blank=True,null=True,)
    email_address = models.EmailField('Email Address',blank=True,null=True,)


class Ethnos(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Education(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class MobiType(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Rang(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Region(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Army(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

class Body(models.Model):
    first_name = models.CharField(max_length=20,blank=True,null=True)
    middle_name = models.CharField(max_length=20,blank=True,null=True)
    last_name = models.CharField(max_length=20)
    region = models.ForeignKey(Region,blank=True,null=True,on_delete=models.SET_NULL)
    army = models.ForeignKey(Army,blank=True,null=True,on_delete=models.SET_NULL)
    creator = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='images/')

    education = models.ForeignKey(Education,blank=True,null=True,on_delete=models.SET_NULL)
    mobitype = models.ForeignKey(MobiType,blank=True,null=True,on_delete=models.SET_NULL)
    rang = models.ForeignKey(Rang,blank=True,null=True,on_delete=models.SET_NULL)
    ethnos = models.ForeignKey(Ethnos,blank=True,null=True,on_delete=models.SET_NULL)

    oririgin_img = models.ImageField('копия экрана',null=True,blank=True,upload_to='images/')
    origin_url = models.URLField('линк-источник',blank=True,null=True,)

    flag_done = models.BooleanField('проверено',default=False)

    birth_date = models.DateField('дата рождения',blank=True,null=True,)
    death_date = models.DateField('дата смерти',blank=True,null=True,)

    birth_place = models.TextField('место рождения',blank=True,null=True,)



    def __str__(self):
        #return self.first_name +  ' ' + self.last_name + ' (' + str(self.id) + ')'
        return self.last_name + ' (' + str(self.id) + ')'
