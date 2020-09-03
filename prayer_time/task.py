from celery import shared_task
from celery.schedules import crontab
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from .models import PrayerTime
import re
from celery.task import periodic_task

def geturl(url):
    try:
         html=urlopen(url)
    except HTTPError  as e:
        return None
    try: 
        bs=BeautifulSoup(html.read(),'html.parser')
        ti = bs.find_all('span',{"class" : "prayertime"})

    except AttributeError as e:
        return None
    return ti 

@periodic_task(run_every=(crontab(minute='*/1')), name="prayer_time_task")
def nadjib():
    ti = geturl('https://www.islamicfinder.org/world/algeria/2507480/algiers-prayer-times/?language=fr')
    time = [t.get_text() for t in ti]
    #na = bs.find_all('span',class_="prayername")
    #name  = [n.get_text() for n in na]
    #attig = tuple(zip(name,time))
    prayer_time = PrayerTime()
    prayer_time.Fajr = time[0]
    prayer_time.Shorouk = time[1]
    prayer_time.Duhr = time[2]
    prayer_time.Asr = time[3]
    prayer_time.Maghrib = time[4]
    prayer_time.Aicha = time[5]
 
    prayer_time.save()


    print('heloo nadjib !')