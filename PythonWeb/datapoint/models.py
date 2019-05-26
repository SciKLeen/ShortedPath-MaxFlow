from django.db import models

# Create your models here.
class data(models.Model):
    point = models.CharField(max_length = 100)
    name = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    latitude = models.FloatField()
    longtitude = models.FloatField()