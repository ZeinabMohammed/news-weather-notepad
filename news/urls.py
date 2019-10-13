from django.urls import path, include
from .views  import *


app_name="news"
urlpatterns = [


	path('', scrape, name='scrape'),

]