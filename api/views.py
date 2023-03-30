from django.http import JsonResponse

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import Http404, HttpResponseRedirect

from .serializers import PostSerializer, CategorySerializer, PostDetailSerializer
from .models import Post, Category

from react_django_blog.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, AWS_STORAGE_BUCKET_NAME, IMAGE_URL
import boto3, uuid

class CategoryView(APIView): # 카테고리 정보 가져오기
    def get_object(self, category_id):
        try:
            return Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_id, format=None):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class CategorysView(APIView): # 카테고리 리스트 정보 가져오기
    def get(self, request, user_id, format=None):
        categorys = Category.objects.filter(user_id=user_id)
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)

class PostCardList(APIView): # 카드 리스트 불러오기
    def get(self, request):
        cards = Post.objects.filter(post_type=1).order_by('-create_at')[:10]
        serializer = PostSerializer(cards, many=True)
        return Response(serializer.data)

class PostList(APIView): # 게시물 리스트 불러오기
    def get(self, request):
        print(request.GET.get('category'))
        posts = Post.objects.filter(category_id=request.GET.get('category')).order_by('-create_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView): # 게시물 디테일 불러오기
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

class PostCreateView(APIView): # 게시물 생성
    def post(self, request):
        try:
            post = Post()

            file = request.FILES.get('thumbnail')
            if file:
                host_id = request.GET.get('host_id')
                s3r = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
                key = "%s"%(host_id)

                file._set_name(str(uuid.uuid4()))
                s3r.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=key+'/%s'%(file), Body=file, ContentType='image/jpeg')

                post.thumbnail = ("%s/%s"%(host_id, file))
                
            post.category_id = request.data['category_id']
            post.title = request.data['title']
            post.content = request.data['content']
            post.post_type = request.data.get('post_type', 0)
            post.bg_color = request.data.get('bg_color', '')
            post.text_color = request.data.get('text_color', '')
            post.save()
            
            return JsonResponse({"message": "success"}, status=200)

        except Exception as e:
            return JsonResponse({"error": e})