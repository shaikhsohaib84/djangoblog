from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    Status_choice=(
        ('ACTIVE','Active'),
        ('INACTIVE','Inactive')
    )
    email = models.EmailField('email_address',unique=True)
    contact = models.TextField(max_length=10,null=True,blank=False)
    description = models.TextField(max_length=60,null=True,blank=False)
    linkedin_url = models.URLField(null=True,blank=True)
    status = models.CharField(max_length=10, null=False, blank=False, choices=Status_choice,default='ACTIVE')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


