from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.prayer_time.as_view()),
    

]