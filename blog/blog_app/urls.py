from django.conf.urls import url
from .views import CreateBlogAPI, BlogListAPI, UpdateBlogStatusAPI

urlpatterns=[
    url('createblog',CreateBlogAPI.as_view()),
    url('draftblog', BlogListAPI.as_view()),
    url('updateblogstatus/(?P<pk>.+)',UpdateBlogStatusAPI.as_view())
]