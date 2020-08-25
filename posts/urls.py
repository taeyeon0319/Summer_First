from django.urls import path
from .views import *

app_name="posts"
urlpatterns = [
    path('new/',new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('show/<int:post_id>/', show, name="show"), # 오오~
    path('update/<int:id>/', update, name="update"), # 여기는? post_id? id? 👏🏻 저장
    path('delete/<int:id>/', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
]