from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostCardList, PostDetail

urlpatterns = [
    # 회원가입 / 로그인
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    path('cards/', PostCardList.as_view()),
    path('posts/', PostCardList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)