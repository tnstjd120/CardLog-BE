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
        fields = ('id', 'name', 'create_at')


# ========== Post Serializers ==========
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_type', 'title', 'content', 'bg_color', 'text_color', 'thumbnail', 'update_at', 'create_at')