from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path

from rest_framework import routers
from .views import PostViewSet

app_name='pictusapp'

router=routers.SimpleRouter()
router.register('posts',PostViewSet)

urlpatterns=router.urls

# urlpatterns=[

#     path('comments/', CommentView.as_view()),
#     path('comments/<int:pk>', CommentDetailView.as_view()),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)