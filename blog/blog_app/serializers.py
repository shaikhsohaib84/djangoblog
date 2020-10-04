from rest_framework import serializers
from .models import blog_app

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_app
        fields = ["id",
                  "user_id",
                  "title",
                  "content",
                  "status",
                  "created_at",
                  "updated_at",
                  ]

class UpdateBlogStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_app
        fields = ["id","status"]