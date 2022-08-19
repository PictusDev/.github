from rest_framework import serializers
from .models import *
from pictususer.serializers import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','author','content','created_at','post','modified_at']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['content','film','camera','image']


class PostSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    # comment=CommentSerializer(many=True, read_only=True)

    class Meta:
        model=Post
        fields=['pk','content','image','like','created_at','profile','film','camera','author']

