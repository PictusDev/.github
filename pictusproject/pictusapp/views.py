from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import *
from pictususer.models import Profile
from rest_framework import views, viewsets
from rest_framework.response import Response 

from .permissions import CustomReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# class PostView(views.APIView):
#     def get(self, request, format=None):
#         posts=Post.objects.all()
#         serializer=PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer=PostCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data)
    
# class PostDetailView(views.APIView):
#     def get(self, request, pk, format=None):
#         post=get_object_or_404(Post, pk=pk)
#         serializer=PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk, formant=None):
#         post=get_object_or_404(Post, pk=pk)
#         serializer=PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk, format=None):
#         post=get_object_or_404(Post, pk=pk)
#         post.delete()
#         return Response()

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    permission_classes=[CustomReadOnly]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=('author','like','film','camera','content','profile','nickname')

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        profile=Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

# class CommentView(views.APIView):
#     def post(self, request, format=None):
#         serializer=CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class CommentDetailView(views.APIView):
#     def get(self, request, pk, format=None):
#         comment=get_object_or_404(Comment, pk=pk)
#         serializer=CommentSerializer(comment)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         comment=get_object_or_404(Comment, pk=pk)
#         serializer=CommentSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk, format=None):
#         comment=get_object_or_404(Comment, pk=pk)
#         comment.delete()
#         return Response()
