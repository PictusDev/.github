from rest_framework import serializers
from pictusapp.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','author','content','created_at','post','modified_at']

class PostCreateSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields=['id','title','content','film','camera','image','hashtag']

class PostSerializer(serializers.Serializer):
    comment=CommentSerializer(many=True, read_only=True)

    class Meta:
        model=Post
        fields=['id','title','content','film','camera','image','like','hashtag','created_at','author','comment']

