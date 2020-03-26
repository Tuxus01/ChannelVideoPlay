from django.contrib import admin
from django.urls import path,include
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from .views import *




urlpatterns = [
    path('', Index, name="index"),
    path('channel/<int:id>/', channelsID ,name='ChannelID'),
   

   
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

