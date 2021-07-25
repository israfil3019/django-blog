from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    user = models.ImageField(upload_to='user', blank=True)

    def __str__(self):
        return self.user.username