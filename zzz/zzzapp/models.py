from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    butter = models.OneToOneField(User)
    profile = models.ImageField(upload_to='picture',blank=True)
    resume = models.FileField(upload_to='file',blank=True)
