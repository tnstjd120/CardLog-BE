from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostCardList, PostList, PostDetail, CategoryView, CategorysView, PostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [

    # Category 관련
    path('categorys/<int:user_id>/', CategorysView.as_view()),
    path('category/<int:category_id>/', CategoryView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/update/', CategoryUpdateView.as_view()),
    path('category/delete/', CategoryDeleteView.as_view()),

    # Post 관련
    path('cards/', PostCardList.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/update/', PostUpdateView.as_view()),
    path('post/delete/', PostDeleteView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)