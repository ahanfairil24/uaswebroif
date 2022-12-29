from django.db import models

class santri(models.Model):
    nama = models.CharField(max_length=100)
    Asatidz = models.CharField(max_length=100)


    

