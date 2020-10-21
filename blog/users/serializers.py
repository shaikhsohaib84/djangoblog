from rest_framework import serializers
from .models import User
#authenticate is imported for login-authenticate
from django.contrib.auth import authenticate

#creating sign up for user using Modelserializer
class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        # to get all the table data from User class and assign to model
        model = User
        # creat list of all fields present in our database
        fields = ["first_name",
                  "last_name",
                  "username",
                  "email",
                  "password",
                  "contact",
                  "description",
                  "linkedin_url",
                  "status"]

    #create function out-side class meta coz create is in-build function of serializer
    # for creating user with the help of serialzer->validate_data, which will add functionality
    def create(self, validate_data):
        user = User.objects.create_user(
            first_name = validate_data.pop('first_name'),
            last_name  = validate_data.pop('last_name'),
            username  = validate_data.pop('username'),
            email  = validate_data.pop('email'),
            password  = validate_data.pop('password'),
            contact  = validate_data.pop('contact'),
            description  = validate_data.pop('description'),
            linkedin_url  = validate_data.pop('linkedin_url'),
            status  = validate_data.pop('status')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    print("email is",email)
    print("password is",password)

    def validate(self, attrs):
        self.user = authenticate(username=attrs.pop("email"),
                                 password=attrs.pop("password"))

        if self.user:
            return attrs
        else:
            raise serializers.ValidationError()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["id", "first_name", "last_name", "email", "description", "linkedin_url", "contact"]
