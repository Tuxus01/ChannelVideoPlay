from django.shortcuts import render
from .models import *
import datetime
from django.http import HttpResponse

#WakeOnLan encendido remoto los tv
from wakeonlan import send_magic_packet
import subprocess as sp
import os

# Create your views here.
def Index(request):
    Canales = channel.objects.all()
    print(Canales)
    ctx = {'CHANNEL': Canales}
    check_ping('192.168.1.1')
    Data = []
    

    return render(request, 'index.html' ,ctx)



def channelsID(request, id):
    try:
        p = channel.objects.get(pk=id)
        video = videoChannel.objects.filter(channel = id).order_by('-id')[0]
        #print(video)
    except channel.DoesNotExist:
        raise Http404("Channel does not exist")
    return render(request, 'channel.html', {'CHANNEL': p})



#Validador de encendido por medio de ping 
def check_ping(hostname):
    response = os.system("ping " + hostname + " -n 1")
    if response == 0:
        print (hostname, 'is up!')
        return 1
    else:
        print (hostname, 'is down!')
        return 0