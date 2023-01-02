from django.urls import path
from app1.views import *
app_name = 'jithu'

urlpatterns = [
    path("ikka/", ikka, name='ikka'),
]
