from .serializers import CreateBlogSerializer,UpdateBlogStatusSerializer
from  rest_framework.generics import (CreateAPIView,
                                      ListAPIView,
                                      UpdateAPIView,)
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import blog_app
# Create your views here.

class CreateBlogAPI(CreateAPIView):
    serializer_class = CreateBlogSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.errors)

class BlogListAPI(ListAPIView):
    serializer_class = CreateBlogSerializer
    queryset = ''
    def post(self, request, *args, **kwargs):

        data = list()
        get_status = request.data["status"]
        blog_data = blog_app.objects.filter(status=get_status)
        serializer = self.get_serializer(blog_data, many=True)

        for blog in serializer.data:
            get_user = User.objects.filter(id=blog["user_id"]).values("first_name",
                                                                      "last_name",
                                                                      "email",
                                                                      "description",
                                                                      "linkedin_url")

            print("USER_DETAILS", get_user)
            data.append({
                "id": blog["id"],
                "title": blog["title"],
                "content": blog["content"],
                "status": blog["status"],
                "user_id": blog["user_id"],
                "created_at": blog["created_at"],
                "updated_at": blog["updated_at"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "description": get_user[0]["description"],
                "linkedin_url": get_user[0]["linkedin_url"]
            })
        return Response(data, status.HTTP_200_OK)

class UpdateBlogStatusAPI(UpdateAPIView):
    serializer_class = UpdateBlogStatusSerializer

    def get_queryset(self):
        blog_id = self.kwargs['pk']
        return blog_app.objects.filter(id=blog_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data['status']

        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)
    
class GetBlogDetailsAPI(ListAPIView):
    serializer_class = CreateBlogSerializer
    queryset = ''
    def get(self, request, *args, **kwargs):
        data = list()
        blog_id = self.kwargs['pk']
        blog_data = blog_app.objects.filter(id = blog_id)
        serializer = self.get_serializer(blog_data, many=True)
        print("serializer data",serializer.data)
        for blog in serializer.data:
            get_user = User.objects.filter(id=blog['user_id']).values("first_name", "last_name", "email", "description", "contact")
            data.append({
                "id":blog['id'],
                "title":blog['content'],
                "status":blog['status'],
                "user_id":blog['user_id'],
                "first_name":get_user[0]['first_name'],
                "last_name": get_user[0]['last_name'],
                "email": get_user[0]['email'],
                "description": get_user[0]['description'],
                "contact": get_user[0]['contact'],
                "created_at": blog['created_at'],
                "updated_at": blog['updated_at']
            })
            return Response(data, status.HTTP_200_OK)
