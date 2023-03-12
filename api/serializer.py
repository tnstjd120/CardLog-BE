from rest_framework import serializers
from .models import Post, User, LinkList, Category

# ========== User Serializers ==========
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'profile_img', 'about', 'blog_name')

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