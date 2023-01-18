from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=64, blank=False, null=False, default='city')
    temp = models.FloatField()
    pressure = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)