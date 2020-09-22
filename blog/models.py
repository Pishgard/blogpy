from django.db import models
from django.contrib.auth import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)

class Article(models.Model):
     title = models.CharField(max_length=128, null=False, blank=False)
     cover = models.FileField(upload_to='filed/article_cover/', null=False, blank=False)
