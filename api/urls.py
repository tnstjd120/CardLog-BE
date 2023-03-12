from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostCardList, PostDetail

urlpatterns = [
    path('cards', PostCardList.as_view()),
    path('posts', PostCardList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)