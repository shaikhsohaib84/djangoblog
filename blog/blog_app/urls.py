from django.conf.urls import url
from .views import CreateBlogAPI

urlpatterns=[
    url('createblog',CreateBlogAPI.as_view())
]