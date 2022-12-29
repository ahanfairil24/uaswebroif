from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', include('about.urls')),
]

#from django.conf.urls import url, include
#from django.contrib import admin 

#urlpatterns =[
#    url(r'^about/', include('about.urls', namespace='about')),
#    url(r'^admin/', admin.site.urls)
#]