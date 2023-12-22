from django.db import models
from django.contrib.auth.models import User

class Art(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dp = models.FileField(upload_to='dp')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    onlyfans = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    insta = models.URLField(null=True, blank=True)


