from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('savedplaylists/', views.savedplaylists, name='savedplaylists'),
]