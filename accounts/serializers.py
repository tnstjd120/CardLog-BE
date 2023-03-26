from rest_framework import serializers
from django.db import transaction
from .models import User
from api.models import Category, LinkList, Post
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer


# 회원가입 custom serializers
class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    blog_id = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'phone', 'blog_id')

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
            'username': self.validated_data.get('username', ''),
            'phone': self.validated_data.get('phone', ''),
            'blog_id': self.validated_data.get('blog_id', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.phone = self.cleaned_data.get('phone')
        user.blog_id = self.cleaned_data.get('blog_id')
        user.save()
        adapter.save_user(request, user, self)
        return user

# 유저정보 custom serializers
class CustomUserDetailSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'profile_img', 'about', 'blog_name', 'blog_id']

# 로그인 custom serializers
# class CustomLoginSerializer(LoginSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'password', 'username', 'phone']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkList
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

# Blog_id로 유저 정보 불러오기
class UserInfoBlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    link_list = LinkListSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_img', 'about', 'phone', 'blog_id', 'blog_name', 'update_at', 'create_at', 'category', 'link_list')