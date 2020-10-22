from django.urls import path, re_path
from . import views


app_name = 'sightings'

urlpatterns = [
        path('', views.list_of_squirrels, name='list_of_squirrels'),
        path('create/', views.create_squirrel, name='create_squirrel'),
        path('stats/', views.stats, name='stats'),
        re_path('^(?P<Unique_Squirrel_ID>[0-9]+.{12})/$', views.detail, name='detail')
]
