from django.urls import path
from . import views

app_name="introduction"
urlpatterns = [
    path('',views.profile, name="home"),
]