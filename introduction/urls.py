from django.urls import path
from . import views

app_name="introduction"
urlpatterns = [
    path('',views.home, name="home"),
    path('activity/', views.activity, name="activity"),
    path('delicious/', views.delicious, name="delicious"),
    path('photo/', views.photo, name="photo"),
]