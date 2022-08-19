from django.urls import URLPattern, path
from .views import *

urlpatterns=[
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<nickname>/',ProfileView.as_view()),
    path('profile/',ProfileListView.as_view()),
]