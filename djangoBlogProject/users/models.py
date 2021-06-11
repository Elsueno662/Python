from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='My name is ...')
    profile_pic = models.ImageField(default='default.jpg', upload_to='images')

    def __str__(self):
        return f'{self.user.username} profile'

