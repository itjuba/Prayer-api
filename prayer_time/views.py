from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .models import PrayerTime
from .serializer import PrayerSerializer
import re
from .task import nadjib
# Create your views here.


class prayer_time(APIView):
    http_method_names = ['get', 'head', 'post']
  

    def get(self, request, *args, **kwargs):
        data = {}
        prayer = PrayerTime.objects.last()
        p_serializer = PrayerSerializer(prayer)
        data['data'] = p_serializer.data
        return Response(data)