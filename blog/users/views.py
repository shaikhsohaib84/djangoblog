from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     GenericAPIView)
from rest_framework.response import Response
from rest_framework import status
from .serializers import (UserSignupSerializer,
                          UserLoginSerializer)
from .models import User

class UserSignupAPIView(CreateAPIView):
    serializer_class = UserSignupSerializer

    def post(self, request, *args, **kwargs):
        print("request data",request.data)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            #to show/cross check that iS DATA has been saved into db
            obj = User.objects.get(email=request.data["email"])

            response_data = {
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email":obj.email,
                "description":obj.description,
                "linkedin_url":obj.linkedin_url,
                "contact":obj.contact,
                "password":obj.password,
                "status":obj.status,
            }
            return Response(response_data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserListAPI(ListAPIView):
    serializer_class = UserSignupSerializer

    def get_queryset(self):
        return User.objects.filter(status='Active')

    def get(self, request, *args, **kwargs):
        serializer =  super().list(request, *args, **kwargs)
        return Response(serializer.data, status.HTTP_302_FOUND)

class UserLoginAPI(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("inside post",request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.user

            response_data = {
                "id":obj.id,
                "email":obj.email,
                "username":obj.username,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
            }
            return Response(response_data, status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)