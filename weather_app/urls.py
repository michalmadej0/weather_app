from django.urls import path
from . import views

app_name ='weather_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load_date, name='load'),
]