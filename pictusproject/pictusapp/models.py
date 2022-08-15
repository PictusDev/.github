
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pictususer.models import Profile

# Create your models here.


class Film(models.Model):
    name=models.CharField(null=False, max_length=100)

class Camera(models.Model):
    name=models.CharField(null=False, max_length=100)

class Hashtag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Post(models.Model):
    image=models.ImageField(null=False, upload_to='pictus_photo')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    film=models.ForeignKey(Film, on_delete=models.CASCADE)
    camera=models.ForeignKey(Camera, on_delete=models.CASCADE)
    like=models.ManyToManyField(User, related_name='like')
    hashtag=models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.image

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    content=models.TextField(null=False)


class Scrap(models.Model):
    title=models.CharField(max_length=100, unique=True)
    post=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


    
