from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostCardList, PostList, PostDetail, CategoryView, CategorysView, PostCreateView

urlpatterns = [
    path('category/<int:category_id>/', CategoryView.as_view()),
    path('categorys/<int:user_id>/', CategorysView.as_view()),
    path('cards/', PostCardList.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('post/create/', PostCreateView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)