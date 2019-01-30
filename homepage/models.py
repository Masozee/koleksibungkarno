from django.db import models

# Create your models here.

class HomeSlide(models.Model):
    slide1 = models.FileField(upload_to='homepage/')
    caption1 = models.CharField(max_length=25, null=True, blank=True)
    subcaption1 = models.CharField(max_length=50, null=True, blank=True)
    link1=models.TextField(null=True, blank=True)
    slide2 = models.FileField(upload_to='homepage/')
    caption2 = models.CharField(max_length=25, null=True, blank=True)
    subcaption2 = models.CharField(max_length=50, null=True, blank=True)
    link2 = models.TextField(null=True, blank=True)
    slide3 = models.FileField(upload_to='homepage/')
    caption3 = models.CharField(max_length=25, null=True, blank=True)
    subcaption3 = models.CharField(max_length=50, null=True, blank=True)
    link3 = models.TextField(null=True, blank=True)

