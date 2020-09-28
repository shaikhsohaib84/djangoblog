from rest_framework import serializers
from .models import blog_app

class CreateBlog(serializers.ModelSerializer):
    class Meta:
        model = blog_app
        fields = ["id",
                  "title",
                  "content",
                  "status",
                  "created_at",
                  "updated_at",
                  "user_id"
                  ]