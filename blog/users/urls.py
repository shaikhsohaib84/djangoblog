from django.conf.urls import url
from .views import HelloWorld
# Create your views here.
urlpatterns = [
    url('HelloWorld',HelloWorld.as_view()),
]