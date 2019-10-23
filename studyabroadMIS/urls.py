from django.urls import path

from . import views

app_name = 'studyabroadMIS'
urlpatterns = [
    path('', views.index, name='index'), 
]