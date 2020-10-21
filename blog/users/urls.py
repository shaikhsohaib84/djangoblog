from django.conf.urls import url
from .views import (UserSignupAPIView, UserListAPI, UserLoginAPI, DeleteUserAPI,UpdateUserAPI)

urlpatterns =[
    url('signup',UserSignupAPIView.as_view()),
    url('userlist',UserListAPI.as_view()),
    url('login',UserLoginAPI.as_view()),
    url('userDelete/(?P<pk>.+)',DeleteUserAPI.as_view()),
    url('userupdate/(?P<pk>.+)',UpdateUserAPI.as_view())
]