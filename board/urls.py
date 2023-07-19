from django.urls import path

from board.views import boards, index, post


urlpatterns=[
    path('',boards, name="boards"),
    path('index/',index),
    path('post/',post,name="post"),
]