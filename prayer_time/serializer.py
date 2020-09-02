from rest_framework import serializers
from .models import PrayerTime

class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerTime
        fields = ('__all__')