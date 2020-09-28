from django.shortcuts import render
from .serializers import CreateBlog
from  rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import blog_app
# Create your views here.

class CreateBlogAPI(CreateAPIView):
    serializer_class = CreateBlog

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.errors)
