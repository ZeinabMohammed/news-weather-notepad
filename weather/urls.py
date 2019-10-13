from django.urls import path, include
from .views  import *


app_name="weather"
urlpatterns = [


	path('', weather, name='weather'),

]