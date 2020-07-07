from django.urls import path
from . import views

app_name="delicious"
urlpatterns = [
    path('',views.profile, name="delicious"),
]