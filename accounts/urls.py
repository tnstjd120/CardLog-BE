from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ConfirmEmailView, CustomUserDetailsView, CustomRegisterView, UserInfoBlogView, ProfileImageUpload

from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView

# JWT CONF
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view

urlpatterns = [
    # 회원가입 / 로그인
    path('auth/', include('dj_rest_auth.urls')),
    path('user/', CustomUserDetailsView.as_view(), name="user_detail"),
    path('register/', CustomRegisterView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/refresh/', TokenRefreshView().as_view(), name='token_refresh'),

    path('user/<slug:blog_id>/', UserInfoBlogView.as_view(), name="user_info_email"),
    path('image/', ProfileImageUpload.as_view(), name="user_upload_image"),

    # Email
    # 이메일 관련 필요
    path('accounts/allauth/', include('allauth.urls')),
    # 유효한 이메일이 유저에게 전달
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
]

urlpatterns = format_suffix_patterns(urlpatterns)