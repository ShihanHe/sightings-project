from django.urls import path, re_path
from . import views


app_name = 'sightings'

urlpatterns = [
        path('', views.list_of_squirrels, name='list_of_squirrels'),
        re_path(r'^.*([1-9].*[1-9]).*$', views.detail, name='detail'),
        path('create/', views.create_squirrel, name='create_squirrel'),
        path('stats/', views.stats, name='stats'),
]
