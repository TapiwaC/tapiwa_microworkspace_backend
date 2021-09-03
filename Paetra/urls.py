from django.urls import path
from . views import create_person 
app_name ='Paetra'
urlpatterns = [
    path('', create_person, name='create_person')
]