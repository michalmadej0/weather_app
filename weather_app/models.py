from django.db import models

class Weather(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)