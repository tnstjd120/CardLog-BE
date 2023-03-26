from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import Http404, HttpResponseRedirect
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView

from .serializers import CustomRegisterSerializer, CustomUserDetailSerializer, UserInfoBlogSerializer, PostSerializer
from .models import User
from api.models import Post

# ============= EMAIL =============
class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        # A React Router Route will handle the failure scenario
        return HttpResponseRedirect('http://localhost:3000/signup/success') # 인증성공

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                # A React Router Route will handle the failure scenario
                return HttpResponseRedirect('/') # 인증실패
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

# ============= Registeration =============
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

# ============= User Detail =============
class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailSerializer

class UserInfoBlogView(APIView): # 블로그 아이디로 유저 정보 불러오기
    def get_object(self, blog_id):
        try:
            return User.objects.prefetch_related('category', 'link_list').get(blog_id=blog_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, blog_id, format=None):
        user = self.get_object(blog_id)
        post = Post.objects.filter(category__user=user, post_type=1)

        serializer = UserInfoBlogSerializer(user, context={'request': request})
        data = serializer.data
        data['post'] = PostSerializer(post, many=True).data
        return Response(data)