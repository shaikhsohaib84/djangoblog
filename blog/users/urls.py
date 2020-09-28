from django.conf.urls import url
from .views import (UserSignupAPIView, UserListAPI, UserLoginAPI)

urlpatterns =[
    url('signup',UserSignupAPIView.as_view()),
    url('userlist',UserListAPI.as_view()),
    url('login',UserLoginAPI.as_view())
]