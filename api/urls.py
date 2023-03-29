from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostCardList, PostList, PostDetail

urlpatterns = [
    path('cards/', PostCardList.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)