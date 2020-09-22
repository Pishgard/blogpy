from django.db import models
from django.contrib.auth import User
from ckeditor.fields import RichTextField
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)

class Article(models.Model):
     title = models.CharField(max_length=128, null=False, blank=False)
     cover = models.FileField(upload_to='filed/article_cover/', null=False, blank=False)
     content = RichTextField()
     created_at = models.DateTimeField(default=datetime, blank=False)
     category = models.ForeignKey('Category', on_delete=models.CASCADE)
     author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/',null=False, blank=False)