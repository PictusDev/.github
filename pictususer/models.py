from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname=models.CharField(max_length=128,null=True)
    url =models.CharField(max_length=128, null=True)
    information =models.CharField(max_length=256, null=True)
    image=models.ImageField(upload_to='profile/', default='default.png')
    email=models.CharField(max_length=128,null=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        

@receiver(pre_save, sender=Profile)
def default_nickname(sender, instance, **kwargs):
     if not instance.nickname:
         instance.nickname = instance.user.username

@receiver(pre_save, sender=Profile)
def default_email(sender, instance, **kwargs):
     if not instance.email:
         instance.email = instance.user.email