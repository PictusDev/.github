from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path

app_name='pictusapp'

urlpatterns=[
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', PostDetailView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>', CommentDetailView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)