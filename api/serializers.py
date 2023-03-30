from rest_framework import serializers
from django.db import transaction
from .models import Post, User, LinkList, Category
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from dj_rest_auth.serializers import UserDetailsSerializer

class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkList
        fields = ('id', 'icon_type', 'url')


# ========== Category Serializers ==========
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# ========== Post Serializers ==========
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  "__all__"

# ========== Post Serializers ==========
class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields =  "__all__"

    def get_user(self, post):
        user = post.category.user
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "blog_id": user.blog_id,
            "profile_img": user.profile_img
        }
