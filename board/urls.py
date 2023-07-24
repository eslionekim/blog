from django.urls import path

from board.views import boards, delete, index, post,update


urlpatterns=[
    path('',boards, name="boards"),
    path('index/',index),
    path('post/',post,name="post"),
    path('update/<int:pk>/',update,name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
]