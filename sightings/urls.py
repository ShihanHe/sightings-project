from django.urls import path
from . import views

urlpatterns = [
        path('', views.list_of_squirrels, name='list_of_squirrels'),
        path('<str:squirrel_id>/', views.update_squirrel, name='update_squirrel'),
        path('create/', views.create_squirrel, name='create_squirrel'),
        path('stats/', views.stats, name='stats'),
]
