from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
# Create your models here.

#Base Global para todas las tablas
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default = True)
    date_create = models.DateField('Date of Create',auto_now = False, auto_now_add = True)
    date_change = models.DateField('Date of Change',auto_now = True, auto_now_add = False)
    date_delete = models.DateField('Date of Delete',auto_now = True, auto_now_add = False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    date_time_c = models.TimeField(auto_now = False, auto_now_add = True)
    date_time_m = models.TimeField(auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True


def RutaVideo(self,filename):
    path = "static/MultimediaData/Video/%s/%s" %(self.date_create, str(filename))
    return path




class videoChannel(ModelBase):
    name = models.CharField('Name Video', max_length=100 )
    description = models.TextField('Description', max_length=1800, blank=True, null=True)
    #channel = models.ForeignKey(channel, on_delete=models.CASCADE)
    video = models.FileField(upload_to=RutaVideo, blank=True, null=True)

    def __str__(self):
        return self.name



class channel(ModelBase):
    name_channel = models.CharField('Name Channel', max_length=80)
    status = models.BooleanField(default=True)
    ip = models.CharField('IP', max_length=16)
    mac = models.CharField('MacAddress' , max_length=20)
    video = models.ForeignKey(videoChannel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_channel

