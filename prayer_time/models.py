from django.db import models

# Create your models here.
class PrayerTime(models.Model):

    Fajr  = models.TimeField()
    Shorouk  = models.TimeField()
    Duhr  = models.TimeField()
    Asr  = models.TimeField()
    Maghrib  = models.TimeField()


    Aicha = models.TimeField()


    def __str__(self):
        return str(self.Maghrib)