from django.urls import path
from app2.views import *
app_name='mahi'
urlpatterns=[
    path('suresh/',suresh,name='suresh'),
    path('naresh/',naresh,name='naresh'),
]