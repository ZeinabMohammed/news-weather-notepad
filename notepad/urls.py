
from django.urls import path
from .views import *
app_name="notes"
urlpatterns = [
    path('create/', create_view, name='create'),

    path('list/', list_view, name='list'),
    path('<id>/delete/', delete_view, name='delete'),

    path('<id>/update/', update_view, name='update'),


]
