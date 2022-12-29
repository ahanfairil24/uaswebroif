from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index),
    
]

#from django.conf.urls import url

#from . import views

#urlpatterns = [
#    url(r'^create/$', views.create, name='create'),
#    url(r'^$', views.index, name='index'),
#]