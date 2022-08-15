from rest_framework import serializers
from pictusapp.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','author','content','created_at','post','modified_at']

class PostCreateSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields=['id','content','film','camera','image','hashtag']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

# {
# "title":"pic",
# "content":"yumi",
# "film":"1",
# "camera":"2",
# "hashtag" :"asd",
# "image":"as"
# }

class PostSerializer(serializers.Serializer):
    comment=CommentSerializer(many=True, read_only=True)

    class Meta:
        model=Post
        fields=['id','content','film','camera','image','like','hashtag','created_at','author','comment']

