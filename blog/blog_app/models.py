from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class blog_app(models.Model):
    blog_status = (
        ('DRAFT','Draft'),
        ('PUBLISHED','Published'),
        ('DELETE','Delete')
    )
    title = models.TextField(max_length=30, null=False, blank=False)
    content = models.TextField(null = False, blank=False)
    status = models.CharField(max_length=10,null=False,blank=False,choices=blog_status, default='DRAFT')
    created_at = models.TimeField(auto_now=timezone.now)
    updated_at = models.TimeField(auto_now=timezone.now)
    user_id = models.ForeignKey(User,null=False, blank=False, on_delete=models.CASCADE)