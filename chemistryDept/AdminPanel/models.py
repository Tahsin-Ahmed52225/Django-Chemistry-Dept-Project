from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.

class Userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_image = models.ImageField(null=True, blank=True, upload_to="Images/")

    def __str__(self):
        return self.user.username
class banner(models.Model) :
    banner_title = models.TextField(max_length=100)
    banner_subtitle = models.TextField(max_length=100)
    banner_description = models.TextField(max_length=100)
    banner_url = models.TextField(max_length=100)
    banner_cover = models.ImageField(null=True, blank=True, upload_to="Images/")
    def __str__(self):
        return self.banner_title
    def banner_info(self):
        banner_info = [self.banner_title , str(self.banner_cover), self.banner_description, self.banner_url, self.banner_subtitle]
        return banner_info
class about(models.Model):
    about_description = models.TextField(max_length=100)
    about_url = models.TextField(max_length=100)
