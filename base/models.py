from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dp = models.FileField(upload_to='dp', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    onlyfans = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    insta = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name



class Art(models.Model):
    prof = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='contents', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    

class Vids(models.Model):
    prof = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)

